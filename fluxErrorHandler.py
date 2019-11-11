
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
import math


class fluxErrorHandler(ErrorListener):
	def __init__(self, output):
		self.output = output
	#tratamento dos erros sintaticos
	def syntaxError(self, recognizer, o, line, column, msg, e):
		#condição ou caracter que gerou o erro sintático
		value = o.text
		#mapeia o tipo de erro sintático ou lexico que aparece
		message = msg
		#print(message)
		if(message[0:11] == "missing '{'"):
			print("Linha " + str(line-1) + ": Condicional não foi aberto corretamente")
		elif(message[0:11] == "missing '}'" or "expecting {'endif', 'else'}" in message):
			print("Linha " + str(line) + ": Condicional não foi fechado corretamente")
		elif("expecting {';', '['}" in message):
			print("Linha " + str(line-1) + ": Faltando ;")
		elif("expecting '=>'" in message):
			print("Linha " + str(line) + ": Faltando {}")
		elif(message[0:10] == "extraneous"):
			print("Linha " + str(line) + ": " + value + " - simbolo nao identificado")
			self.output.write("Linha " + str(line) + ": " + value + " - simbolo nao identificado\n")
		elif(message[18:22] == "goto"):
			print("Linha " + str(line) + ": comando goto deve receber um label")
		elif(message[0:10] == "mismatched"):
			print("Linha " + str(line) + ": esperando STRING, recebeu " + value)
		self.output.write("Fim da compilacao\n")
		#print("Fim da compilacao")
		exit()	
