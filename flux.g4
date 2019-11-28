grammar flux;

fluxograma : grafo EOF ;
grafo :caixa retorno?;
caixa :decisao | label | loop |acao;
decisao : cmdSe | cmdSwitch;
retorno : 'return' ';' |'return' caixa;
cmdSe : 'if' condicao subgrafo cmdElse? 'endif';
cmdElse: 'else' subgrafo;
cmdSwitch : 'switch' condicao '{' casos '}';
casos : caso+;
caso : STRING implicacao;
implicacao : OPSETA subgrafo ('break' ';')?;
condicao : '(' STRING ')' ;
subgrafo : '{'  grafo '}';
label : NOME_LABEL ':' grafo?;
loop : 'goto' NOME_LABEL ';' | 'loop' NOME_LABEL ';';
acao : STRING ('['STRING']')? ';' grafo?;

OPSETA: '=>' ;
STRING : '"' ~('"')* '"';
NOME_LABEL : ([a-zA-Z] | '_')( [a-zA-Z] | [0-9] | '_')*;
WS : [ \t\r\n]+ -> skip ;

ErrorChar: .;