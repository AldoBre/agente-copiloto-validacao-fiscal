from rest_framework import serializers

from .models import Documento, FonteConhecimento, RegraParametrizacao


class FonteConhecimentoSerializer(serializers.ModelSerializer):
    total_documentos = serializers.SerializerMethodField()
    total_trechos = serializers.SerializerMethodField()
    tipo_label = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = FonteConhecimento
        fields = [
            "id",
            "nome",
            "tipo",
            "tipo_label",
            "url",
            "urls",
            "descricao",
            "seguir_links",
            "profundidade_max",
            "ativo",
            "ultima_ingestao_em",
            "ultima_ingestao_ok",
            "ultima_ingestao_detalhe",
            "criado_em",
            "total_documentos",
            "total_trechos",
        ]
        read_only_fields = [
            "ultima_ingestao_em",
            "ultima_ingestao_ok",
            "ultima_ingestao_detalhe",
            "criado_em",
        ]

    def get_total_documentos(self, obj) -> int:
        return obj.documentos.count()

    def get_total_trechos(self, obj) -> int:
        from .models import Trecho

        return Trecho.objects.filter(documento__fonte=obj).count()


class DocumentoSerializer(serializers.ModelSerializer):
    fonte_nome = serializers.CharField(source="fonte.nome", read_only=True)
    total_trechos = serializers.SerializerMethodField()

    class Meta:
        model = Documento
        fields = ["id", "fonte", "fonte_nome", "titulo", "url", "criado_em", "total_trechos"]

    def get_total_trechos(self, obj) -> int:
        return obj.trechos.count()


class RegraParametrizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegraParametrizacao
        fields = [
            "id",
            "campo",
            "categoria",
            "area",
            "orientacao",
            "referencia_url",
            "observacoes",
            "atualizado_em",
        ]
