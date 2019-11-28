from antlr4 import *
from fluxLexer import fluxLexer
from fluxListener import fluxListener
from fluxParser import fluxParser
from fluxVisitor import fluxVisitor
from fluxErrorHandler import fluxErrorHandler
from fluxSemantics import fluxSemantics
import argparse

parser = argparse.ArgumentParser(description='Compiler for fluxograms made with the FluX language', add_help=True)
#parser.add_argument('-f','--file', dest='filepath', type=str, required=True)
parser.add_argument('sourcefile', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

#abrir arquivo de saída 
saida = open(args.output, "w+")

# Parsear texto
if(args.sourcefile != None):
	text = FileStream(args.sourcefile, encoding = 'UTF-8')

# Análise léxica
try:
	lexer = fluxLexer(text)
except ParseCancellationException as pce:
	msg = pce.get_message()

stream = CommonTokenStream(lexer)

# Análise sintática
parser = fluxParser(stream)
#tratamento de erros sintáticos (implementado em fluxErrorHandler)
parser._listeners = [fluxErrorHandler(saida)]
tree = parser.fluxograma()

# Análise semântica
semantic = fluxSemantics()
semantic.visit(tree)

#abrir arquivo de saída semântica
#saida_semantic = open(args.output, "w+")

#tratamento de erros semanticos (implementado em fluxSemantics)
if(semantic.errors):
	#saida_semantic.write(semantic.errors)
	#saida_semantic.write("Fim da compilacao\n")
	print(semantic.errors)
	print("Fim da compilacao\n")
	exit()
else:
	print(semantic.nodesList)
	exit()
