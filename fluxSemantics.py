from antlr4 import *
from fluxListener import fluxListener
from fluxParser import fluxParser
from fluxVisitor import fluxVisitor
import re #Regular expressions
import pydot

class fluxSemantics(fluxVisitor):
	errors = ""
	tabelaLabels = {}
	nicknamesDictionary = {}
	nodesList = {}
	boxList = {}

	def draw(self):
		#debug
		print('labels',self.tabelaLabels)
		print('nicknames',self.nicknamesDictionary)
		print('nodes',self.nodesList)
		print('boxs',self.boxList)
		print('------')
		for k in self.nodesList:
			print(self.nodesList[k])
		print('------')
		#debug

		graph = pydot.Dot(graph_type='digraph')
		visualNodes = {}
		for box in self.boxList.keys():
			if (self.boxList[box] == "box"):
				visualNodes[box] = pydot.Node(box, style="filled", fillcolor="lightblue2",shape=self.boxList[box])
			else:
				visualNodes[box] = pydot.Node(box, style="filled", fillcolor="orange1",shape=self.boxList[box])
			graph.add_node(visualNodes[box])

		for father in self.nodesList.keys():
			for (son,slabel) in self.nodesList[father]:
				graph.add_edge(pydot.Edge(visualNodes[father], visualNodes[son] , label=slabel if slabel!=None else ' '))
			print(son,slabel)
		print('++++')
		print(graph.to_string())
		print('++++')
		graph.write_png('grafo.png')


	# Visit a parse tree produced by fluxParser#fluxograma.

	def visitFluxograma(self, ctx:fluxParser.FluxogramaContext):
		self.visitGrafo(ctx.grafo())
		self.draw()


	# Visit a parse tree produced by fluxParser#grafo.

	def visitGrafo(self, ctx:fluxParser.GrafoContext, label = None, father = None, nickname = None):
		self.visitCaixa(ctx.caixa(), label, father, nickname)
		if (ctx.retorno() != None):
			self.visitRetorno(ctx.retorno())


	# Visit a parse tree produced by fluxParser#caixa.

	def visitCaixa(self, ctx:fluxParser.CaixaContext, label = None, father = None, nickname = None):
		if (ctx.decisao() != None):
			self.visitDecisao(ctx.decisao(), label, father, nickname)
		if (ctx.label() != None):
			self.visitLabel(ctx.label(), label, father)
		if (ctx.loop() != None):
			self.visitLoop(ctx.loop(), label, father)
		if (ctx.acao() != None):
			self.visitAcao(ctx.acao(), label, father, nickname)

	# Visit a parse tree produced by fluxParser#decisao.

	def visitDecisao(self, ctx:fluxParser.DecisaoContext, label = None, father = None, nickname = None):
		if (ctx.cmdSe() != None):
			self.visitCmdSe(ctx.cmdSe(), label, father, nickname)
		if (ctx.cmdSwitch() != None):
			self.visitCmdSwitch(ctx.cmdSwitch(), label, father, nickname)

	# Visit a parse tree produced by fluxParser#retorno.

	def visitRetorno(self, ctx:fluxParser.RetornoContext):
		if(ctx.caixa() != None):
			self.visitCaixa(ctx.caixa())

	# Visit a parse tree produced by fluxParser#cmdSe.

	def visitCmdSe(self, ctx:fluxParser.CmdSeContext, label = None, father = None, nickname = None):
		fatherName = self.visitCondicao(ctx.condicao(), label, father, nickname)
		self.visitSubgrafo(ctx.subgrafo(), "True", fatherName)
		if(ctx.cmdElse() != None):
			self.visitCmdElse(ctx.cmdElse(), fatherName)

	# Visit a parse tree produced by fluxParser#cmdElse.

	def visitCmdElse(self, ctx:fluxParser.CmdElseContext, father = None):
		self.visitSubgrafo(ctx.subgrafo(), "False", father)

	# Visit a parse tree produced by fluxParser#cmdSwitch.

	def visitCmdSwitch(self, ctx:fluxParser.CmdSwitchContext, label = None, father = None, nickname = None):
		fatherName = self.visitCondicao(ctx.condicao(), father, nickname)
		self.visitCasos(ctx.casos(), fatherName)

	# Visit a parse tree produced by fluxParser#casos.

	def visitCasos(self, ctx:fluxParser.CasosContext, father = None):
		if(len(ctx.caso()) < 2):
			self.errors += "Linha " + str(ctx.caso(0).start.line) + ": switches tem de ter ao menos dois casos.\n"
		else:
			tabelaCasos = {}
			for case in ctx.caso():
				caseName = self.visitCaso(case, father)
				if(caseName not in tabelaCasos.keys()):
					tabelaCasos[caseName] = True
				else:
					self.errors += "Linha " + str(case.start.line) + ": caso já definido anteriormente.\n"

	# Visit a parse tree produced by fluxParser#caso.

	def visitCaso(self, ctx:fluxParser.CasoContext, father = None):
		self.visitImplicacao(ctx.implicacao(), ctx.STRING().getText(), father)
		return ctx.STRING().getText()

	# Visit a parse tree produced by fluxParser#implicacao.

	def visitImplicacao(self, ctx:fluxParser.ImplicacaoContext, label = None, father = None):
		self.visitSubgrafo(ctx.subgrafo(), label, father)

	# Visit a parse tree produced by fluxParser#condicao.

	def visitCondicao(self, ctx:fluxParser.CondicaoContext, label = None, father = None, nickname = None):
		self.boxList[ctx.STRING().getText()] = "diamond"

		if(father != None):
			if(father in self.nodesList.keys()):
				self.nodesList[father].append((ctx.STRING().getText(), label))
			else:
				self.nodesList[father] = [(ctx.STRING().getText(), label)]

		if(nickname != None):
			self.nicknamesDictionary[nickname] = ctx.STRING().getText()
			print(f"Nickname: {nickname}")
		print("Condition: " + ctx.STRING().getText())
		if(label != None):
			print(f"Label: {label}")
		if(father != None):
			print(f"Father: {father}")
		print("\n")
		return ctx.STRING().getText()

	# Visit a parse tree produced by fluxParser#subgrafo.

	def visitSubgrafo(self, ctx:fluxParser.SubgrafoContext, label = None, father = None):
		self.visitGrafo(ctx.grafo(), label, father)

	# Visit a parse tree produced by fluxParser#label.

	def visitLabel(self, ctx:fluxParser.LabelContext, label = None, father = None):
		if(ctx.NOME_LABEL().getText() not in self.tabelaLabels.keys()):
			self.tabelaLabels[ctx.NOME_LABEL().getText()] = True
		else:
			self.errors += "Label " + str(ctx.NOME_LABEL().getText()) + ": já definida anteriormente.\n"
		if(ctx.grafo() != None):
			self.visitGrafo(ctx.grafo(), label, father, ctx.NOME_LABEL().getText())
		return

	# Visit a parse tree produced by fluxParser#loop.

	def visitLoop(self, ctx:fluxParser.LoopContext, label = None, father = None):
		if(father != None):
			if(father in self.nodesList.keys()):
				self.nodesList[father].append((self.nicknamesDictionary[ctx.NOME_LABEL().getText()], label))
			else:
				self.nodesList[father] = [(self.nicknamesDictionary[ctx.NOME_LABEL().getText()], label)]
		return

	# Visit a parse tree produced by fluxParser#acao.

	def visitAcao(self, ctx:fluxParser.AcaoContext, label = None, father = None, nickname = None):
		self.boxList[ctx.STRING()[0].getText()] = "box"

		if(father != None):
			if(father in self.nodesList.keys()):
				self.nodesList[father].append((ctx.STRING()[0].getText(), label))
			else:
				self.nodesList[father] = [(ctx.STRING()[0].getText(), label)]

		if(nickname != None):
			self.nicknamesDictionary[nickname] = ctx.STRING()[0].getText()
			print(f"Nickname: {nickname}")
		print("Action: " + ctx.STRING()[0].getText())
		if(label != None):
			print(f"Label: {label}")
		if(father != None):
			print(f"Father: {father}")
		print("\n")
		if(ctx.grafo() != None):
			if(len(ctx.STRING()) > 1):
				self.visitGrafo(ctx.grafo(), ctx.STRING()[1].getText(), ctx.STRING()[0].getText())
			else:
				self.visitGrafo(ctx.grafo(), None, ctx.STRING()[0].getText())
		return
