# Processar

> **Fonte:** Web service Com.senior.g5.co.mct.imp.exclusaocalculo — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mct_imp_exclusaocalculo.htm  
> **Trilha:** Integrações com outros sistemas > Web services > Web services disponíveis no Gestão Empresarial  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Processar

**Necessita autenticação:** Sim.

**Situação da versão:** Atual.

**Versão:** 1.

## Requisição:

```

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.senior.com.br">
  <soapenv:Body>
    <ser:Processar>
      <user>String</user>
      <password>String</password>
      <encryption>Integer</encryption>
      <parameters>
        <imposto>
          <codEmp>Integer</codEmp>
          <codFil>Integer</codFil>
          <codImp>String</codImp>
        </imposto>
      </parameters>
    </ser:Processar>
  </soapenv:Body>
</soapenv:Envelope>
```

## Parâmetros da requisição:

| Nome | Preenchimento | Tipo | Descrição |
| --- | --- | --- | --- |
| imposto | Opcional | Set | - |
| imposto.codEmp | Opcional | Integer | Number(004) - Código da empresa |
| imposto.codFil | Opcional | Integer | Number(004) - Código da filial |
| imposto.codImp | Opcional | String | String(003) - Código do imposto |

## Resposta:

Observação

Envelope SOAP de resposta de requisições síncronas. Para requisições assíncronas ou agendamentos, a resposta é apenas uma String chamada "result" com o valor "OK", se foi executado com sucesso ou, caso contrário, a mensagem do erro ocorrido.

```

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.senior.com.br">
  <soapenv:Body>
    <ser:ProcessarResponse>
      <result>
        <retorno>
          <codEmp>Integer</codEmp>
          <codFil>Integer</codFil>
          <codImp>String</codImp>
          <tipRet>Integer</tipRet>
          <desRet>String</desRet>
        </retorno>
        <erroExecucao>String</erroExecucao>
      </result>
    </ser:ProcessarResponse>
  </soapenv:Body>
</soapenv:Envelope>
```

## Atributos da resposta:

| Nome | Preenchimento | Tipo | Descrição |
| --- | --- | --- | --- |
| retorno | Opcional | Set | - |
| retorno.codEmp | Opcional | Integer | Number(004) - Código da empresa |
| retorno.codFil | Opcional | Integer | Number(004) - Código da filial |
| retorno.codImp | Opcional | String | String(003) - Código do imposto |
| retorno.tipRet | Opcional | Integer | Number(001) - Tipo de Retorno de Processamento: 1 = Processado com sucesso, 2 = Ocorreram erros |
| retorno.desRet | Opcional | String | Detalhamento do retorno |
| erroExecucao | Opcional | String | - |
