from rest_framework import serializers

from .catalogo import (
    CHAT,
    EMBEDDING,
    buscar_modelo,
    embedding_padrao,
    rotulo_do_modelo,
    rotulo_do_provedor,
)
from .models import ProvedorIA


class ProvedorIASerializer(serializers.ModelSerializer):
    """
    O consultor informa só três coisas: **provedor, modelo e chave**.

    Tipo, teto de tokens, temperatura e timeout vêm do catálogo — deixá-los
    editáveis só cria maneira de degradar a resposta sem perceber. O apelido é
    gerado a partir do modelo escolhido.
    """

    api_key = serializers.CharField(
        write_only=True, required=False, allow_blank=True, trim_whitespace=True
    )
    #: Atalho: cadastra também o modelo de embeddings do mesmo provedor,
    #: reaproveitando a credencial. Nenhum modelo faz as duas coisas — chat e
    #: embeddings são endpoints distintos — mas a chave é uma só.
    tambem_embeddings = serializers.BooleanField(write_only=True, required=False, default=False)
    embedding_criado = serializers.SerializerMethodField()
    api_key_mascarada = serializers.CharField(read_only=True)
    tem_chave = serializers.BooleanField(read_only=True)
    nome = serializers.CharField(read_only=True)
    provedor_label = serializers.SerializerMethodField()
    modelo_label = serializers.SerializerMethodField()
    tipo_label = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = ProvedorIA
        fields = [
            "id",
            "nome",
            "provedor",
            "provedor_label",
            "tipo",
            "tipo_label",
            "modelo",
            "modelo_label",
            "api_key",
            "tambem_embeddings",
            "embedding_criado",
            "api_key_mascarada",
            "tem_chave",
            "max_tokens",
            "ativo",
            "padrao",
            "ultimo_teste_em",
            "ultimo_teste_ok",
            "ultimo_teste_detalhe",
            "criado_em",
        ]
        read_only_fields = [
            "tipo",
            "max_tokens",
            "ultimo_teste_em",
            "ultimo_teste_ok",
            "ultimo_teste_detalhe",
            "criado_em",
        ]

    def get_provedor_label(self, obj) -> str:
        return rotulo_do_provedor(obj.provedor)

    def get_modelo_label(self, obj) -> str:
        return rotulo_do_modelo(obj.provedor, obj.modelo)

    def get_embedding_criado(self, obj) -> str | None:
        """Preenchido só na resposta do POST que criou o par chat + embeddings."""
        return getattr(obj, "_embedding_criado", None)

    # ------------------------------------------------------------ validação --
    def validate(self, dados):
        provedor = dados.get("provedor") or getattr(self.instance, "provedor", None)
        modelo = dados.get("modelo") or getattr(self.instance, "modelo", None)
        if buscar_modelo(provedor, modelo) is None:
            raise serializers.ValidationError(
                {"modelo": "Modelo não disponível para este provedor."}
            )
        return dados

    def _nome_unico(self, provedor: str, modelo: str, pk=None) -> str:
        base = f"{rotulo_do_provedor(provedor)} · {rotulo_do_modelo(provedor, modelo)}"[:70]
        candidato, contador = base, 2
        consulta = ProvedorIA.objects.exclude(pk=pk) if pk else ProvedorIA.objects.all()
        while consulta.filter(nome=candidato).exists():
            candidato = f"{base} ({contador})"
            contador += 1
        return candidato

    # --------------------------------------------------------------- escrita --
    def _garantir_embedding(self, provedor: str, chave: str) -> str | None:
        """
        Cadastra (ou atualiza) o modelo de embeddings do provedor com a mesma
        chave. Devolve o rótulo criado, ou ``None`` se o provedor não tiver
        modelo de embeddings — a Anthropic, por exemplo, não publica um.
        """
        modelo_id = embedding_padrao(provedor)
        # O Foundry é o único sem chave aqui: ela vem do ambiente, e o registro
        # existe só para o modelo poder ser escolhido.
        if not modelo_id or (not chave and provedor != "azure"):
            return None

        existente = ProvedorIA.objects.filter(
            provedor=provedor, modelo=modelo_id, tipo=EMBEDDING
        ).first()
        alvo = existente or ProvedorIA(provedor=provedor, modelo=modelo_id)
        alvo.api_key = chave
        alvo.ativo = True
        alvo.padrao = True
        alvo.nome = alvo.nome or self._nome_unico(provedor, modelo_id, pk=alvo.pk)
        alvo.aplicar_catalogo()
        alvo.full_clean()
        alvo.save()
        return rotulo_do_modelo(provedor, modelo_id)

    def create(self, validated_data):
        chave = validated_data.pop("api_key", "")
        tambem_embeddings = validated_data.pop("tambem_embeddings", False)

        instancia = ProvedorIA(**validated_data)
        instancia.nome = self._nome_unico(instancia.provedor, instancia.modelo)
        if chave:
            instancia.api_key = chave
        instancia.aplicar_catalogo()
        instancia.full_clean()
        instancia.save()

        instancia._embedding_criado = None
        if tambem_embeddings and instancia.tipo == CHAT:
            instancia._embedding_criado = self._garantir_embedding(instancia.provedor, chave)
        return instancia

    def update(self, instancia, validated_data):
        chave = validated_data.pop("api_key", "")
        tambem_embeddings = validated_data.pop("tambem_embeddings", False)
        if chave:
            instancia.api_key = chave
        for campo, valor in validated_data.items():
            setattr(instancia, campo, valor)
        instancia.nome = self._nome_unico(instancia.provedor, instancia.modelo, pk=instancia.pk)
        instancia.aplicar_catalogo()
        instancia.full_clean()
        instancia.save()

        instancia._embedding_criado = None
        if tambem_embeddings and chave and instancia.tipo == CHAT:
            instancia._embedding_criado = self._garantir_embedding(instancia.provedor, chave)
        return instancia
