grammar flux;

fluxograma : {print('fluxograma')} grafo+ {print('cabou')}EOF ;
grafo : {print('grafo')}caixa+ retorno?;
caixa :  {print('caixadecisao')}decisão | label | loop | {print('caixacao')}ação | subgrafo;
decisão : cmdSe | cmdSwitch;
retorno : {print('return1')} 'return' ';' | {print('return1')}'return' caixa;
cmdSe : 'if' {print('if')}condição {print('aqui')}  caixa {print('saiusubgrafo')}cmdElse? 'endif';
cmdElse:  {print('else')} 'else' caixa;
cmdSwitch : {print('switch')}'switch' condição '{' casos '}';
casos : caso+ implicação?;
caso : FRASE {print($FRASE)}implicação;
implicação : OPSETA caixa ('break' ';')?;
condição : '(' FRASE ')' {print('condicao',$FRASE)}| FRASE{print('condicao',$FRASE)};
subgrafo : {print('subgrafo')}'{'  grafo '}';
label : NOME_LABEL ':' {print('LABEL:',$NOME_LABEL)};
loop : 'goto' NOME_LABEL {print('goto: ',$NOME_LABEL)} | loop NOME_LABEL {print('loop: ',$NOME_LABEL)};
ação : FRASE {print('acao',$FRASE)}('['FRASE']')? ';';

OPSETA: '=>' ;
STRING : '"' ~('"')* '"';
NOME_LABEL : ([a-zA-Z] | '_')( [a-zA-Z] | [0-9] | '_')*;
FRASE : PALAVRA  (' ' PALAVRA)*  ;
fragment PALAVRA : ~(' '|'('|')'|'\n'|';'|'{'|'}'|'['|']'|'\r'|'\t'|'='|'>'|':')+ ;
WS : [ \t\r\n]+ -> skip ;

ErrorChar: .;
