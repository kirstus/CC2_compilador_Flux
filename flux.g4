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
caso : STRING {print($STRING)}implicação;
implicação : OPSETA caixa ('break' ';')?;
condição : '(' STRING ')' {print('condicao',$STRING)}| STRING{print('condicao',$STRING)};
subgrafo : {print('subgrafo')}'{'  grafo '}';
label : NOME_LABEL ':' {print('LABEL:',$NOME_LABEL)};
loop : 'goto' NOME_LABEL {print('goto: ',$NOME_LABEL)} | loop NOME_LABEL {print('loop: ',$NOME_LABEL)};
ação : STRING {print('acao',$STRING)}('['STRING']')? ';';

OPSETA: '=>' ;
STRING : '"' ~('"')* '"';
NOME_LABEL : ([a-zA-Z] | '_')( [a-zA-Z] | [0-9] | '_')*;
WS : [ \t\r\n]+ -> skip ;

ErrorChar: .;
