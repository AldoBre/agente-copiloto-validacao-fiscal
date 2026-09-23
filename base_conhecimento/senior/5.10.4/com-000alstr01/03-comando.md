# Comando

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr01.htm  
> **Trilha:**   
> **Telas citadas:** E000IPC, E070FIL, E095FOR, E440NFC  
> **Identificadores de regras:** —

---
|  |
| --- |
| ``` SqL_DefinirComando(xCursor, "SELECT                                                                             \  		E000IPC.NOPPRO, E000IPC.CODSTR, E000IPC.ORIMER, E000IPC.VLRIPI, E000IPC.VLRICS, \ 		E000IPC.CODTST, E000IPC.VLRICM, E000IPC.GENA01, E000IPC.VLRIDF, E440NFC.DATEMI  \ 	FROM                                                                              \ 		E440NFC                                                                         \     INNER JOIN E095FOR ON (E095FOR.CODFOR = E440NFC.CODFOR)                         \     INNER JOIN E070FIL ON (E070FIL.CODEMP = E440NFC.CODEMP AND                      \                            E070FIL.CODFIL = E440NFC.CODFIL)                         \     INNER JOIN E000IPC ON (E000IPC.CGCFIL = E070FIL.NUMCGC AND                      \                             E000IPC.CGCFOR = E095FOR.CGCCPF AND                      \                              E000IPC.CHVNEL = E440NFC.CHVNEL)                         \ 	WHERE                                                                             \ 				E440NFC.CODEMP = :pCodEmp                                                   \ 		AND E440NFC.CODFIL = :pCodFil                                                   \ 		AND E440NFC.CODFOR = :pCodFor                                                   \ 		AND E440NFC.NUMNFC = :pNumNfc                                                   \ 		AND E440NFC.CODSNF = :pCodSnf                                                   \ 		AND E000IPC.SEQIPC = :pSeqIte");  Sql_DefinirInteiro(xCursor,"pCodEmp",VSCodEmp); Sql_DefinirInteiro(xCursor,"pCodFil",VSCodFil); Sql_DefinirInteiro(xCursor,"pCodFor",VSCodFor); Sql_DefinirInteiro(xCursor,"pNumNfc",VSNumero); Sql_DefinirAlfa(xCursor,"pCodSnf",VSCodSnf); Sql_DefinirInteiro(xCursor,"pSeqIte",VSSeqIte);  SQL_AbrirCursor(xCursor); ``` |
