grammar flux;

fluxograma : {print('fluxograma')} grafo+ {print('Fim')}EOF ;
grafo : {print('grafo')}caixa+ retorno?;
caixa :  {print('caixadecisao')}decisao | label | loop | {print('caixacao')}acao;
decisao : cmdSe | cmdSwitch;
retorno : {print('return1')} 'return' ';' | {print('return1')}'return' caixa;
cmdSe : 'if' {print('if')}condicao {print('aqui')}  subgrafo {print('saiusubgrafo')}cmdElse? 'endif';
cmdElse:  {print('else')} 'else' subgrafo;
cmdSwitch : {print('switch')}'switch' condicao '{' casos '}';
casos : caso+ implicacao?;
caso : STRING {print($STRING)}implicacao;
implicacao : OPSETA subgrafo ('break' ';')?;
condicao : '(' STRING ')' {print('condicao',$STRING)};
subgrafo : {print('subgrafo')}'{'  grafo '}';
label : NOME_LABEL ':' {print('LABEL:',$NOME_LABEL)};
loop : 'goto' NOME_LABEL {print('goto: ',$NOME_LABEL)} ';' | 'loop' NOME_LABEL ';' {print('loop: ',$NOME_LABEL)};
acao : STRING {print('acao',$STRING)}('['STRING']')? ';';

OPSETA: '=>' ;
STRING : '"' ~('"')* '"';
NOME_LABEL : ([a-zA-Z] | '_')( [a-zA-Z] | [0-9] | '_')*;
WS : [ \t\r\n]+ -> skip ;

ErrorChar: .;