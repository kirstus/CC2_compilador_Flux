# Compilador linguagem Flux

Compilador de código imperativo para criação de fluxogramas.

Instalar o [ANTLR4](https://www.antlr.org/)

Em particular para linux:
```
$ cd /usr/local/lib
$ wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.7.2-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```
Para usar o ANTLR4 com python3:
`pip install antlr4-python3-runtime`

Para gerar os arquivos necessários a partir da gramática:
`$ antlr4 -Dlanguage=Python3 flux.g4 -visitor`

Para executar um dos casos de teste:
`$ python fluxCompiler.py casosDeTeste/{nomeDoCaso}.txt /caminho/do/arquivo/de/saida`
