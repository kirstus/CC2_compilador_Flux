from antlr4 import *
from fluxListener import fluxListener
from fluxParser import fluxParser
from fluxVisitor import fluxVisitor
import re #Regular expressions

class fluxSemantics(fluxVisitor):
	errors = ""
	tabelaLabels = {}

	 # Visit a parse tree produced by fluxParser#fluxograma.

	def visitFluxograma(self, ctx:fluxParser.FluxogramaContext):
		self.visitGrafo(ctx.grafo())

	# Visit a parse tree produced by fluxParser#grafo.

	def visitGrafo(self, ctx:fluxParser.GrafoContext, subgraphType = None):
		self.visitCaixa(ctx.caixa(), subgraphType)
		if (ctx.retorno() != None):
			self.visitRetorno(ctx.retorno())


	# Visit a parse tree produced by fluxParser#caixa.

	def visitCaixa(self, ctx:fluxParser.CaixaContext, subgraphType = None):
		if (ctx.decisao() != None):
			self.visitDecisao(ctx.decisao(), subgraphType)
		if (ctx.label() != None):
			self.visitLabel(ctx.label())
		if (ctx.loop() != None):
			self.visitLoop(ctx.loop())
		if (ctx.acao() != None):
			self.visitAcao(ctx.acao(), subgraphType)

	# Visit a parse tree produced by fluxParser#decisao.

	def visitDecisao(self, ctx:fluxParser.DecisaoContext, subgraphType = None):
		if (ctx.cmdSe() != None):
			self.visitCmdSe(ctx.cmdSe(), subgraphType)
		if (ctx.cmdSwitch() != None):
			self.visitCmdSwitch(ctx.cmdSwitch(), subgraphType)

	# Visit a parse tree produced by fluxParser#retorno.

	def visitRetorno(self, ctx:fluxParser.RetornoContext):
		if(ctx.caixa() != None):
			self.visitCaixa(ctx.caixa())

	# Visit a parse tree produced by fluxParser#cmdSe.

	def visitCmdSe(self, ctx:fluxParser.CmdSeContext, subgraphType = None):
		self.visitCondicao(ctx.condicao(), subgraphType)
		self.visitSubgrafo(ctx.subgrafo(), "True")
		if(ctx.cmdElse() != None):
			self.visitCmdElse(ctx.cmdElse())

	# Visit a parse tree produced by fluxParser#cmdElse.

	def visitCmdElse(self, ctx:fluxParser.CmdElseContext):
		self.visitSubgrafo(ctx.subgrafo(), "False")

	# Visit a parse tree produced by fluxParser#cmdSwitch.

	def visitCmdSwitch(self, ctx:fluxParser.CmdSwitchContext, subgraphType = None):
		self.visitCondicao(ctx.condicao())
		self.visitCasos(ctx.casos())

	# Visit a parse tree produced by fluxParser#casos.

	def visitCasos(self, ctx:fluxParser.CasosContext):
		if(len(ctx.caso()) < 2):
			self.errors += "Linha " + str(ctx.caso(0).start.line) + ": switches tem de ter ao menos dois casos.\n"
		else:
			tabelaCasos = {}
			for case in ctx.caso():
				caseName = self.visitCaso(case)
				if(caseName not in tabelaCasos.keys()):
					tabelaCasos[caseName] = True
				else:
					self.errors += "Linha " + str(case.start.line) + ": caso já definido anteriormente.\n"
			if(ctx.implicacao() != None):
				self.visitImplicacao(ctx.implicacao()) 

	# Visit a parse tree produced by fluxParser#caso.

	def visitCaso(self, ctx:fluxParser.CasoContext):
		self.visitImplicacao(ctx.implicacao())
		return ctx.STRING().getText()

	# Visit a parse tree produced by fluxParser#implicacao.

	def visitImplicacao(self, ctx:fluxParser.ImplicacaoContext):
		self.visitSubgrafo(ctx.subgrafo())

	# Visit a parse tree produced by fluxParser#condicao.

	def visitCondicao(self, ctx:fluxParser.CondicaoContext, subgraphType = None):
		print("Condition: " + ctx.STRING().getText())
		if(subgraphType != None):
			print(f"Label: {subgraphType}")
		return

	# Visit a parse tree produced by fluxParser#subgrafo.

	def visitSubgrafo(self, ctx:fluxParser.SubgrafoContext, subgraphType = None):
		self.visitGrafo(ctx.grafo(), subgraphType)

	# Visit a parse tree produced by fluxParser#label.

	def visitLabel(self, ctx:fluxParser.LabelContext):
		if(ctx.NOME_LABEL().getText() not in self.tabelaLabels.keys()):
			self.tabelaLabels[ctx.NOME_LABEL().getText()] = True
		else:
			self.errors += "Linha " + str(ctx.NOME_LABEL().start.line) + ": label já definida anteriormente.\n"
		print(ctx.NOME_LABEL().getText())
		return

	# Visit a parse tree produced by fluxParser#loop.

	def visitLoop(self, ctx:fluxParser.LoopContext):
		return

	# Visit a parse tree produced by fluxParser#acao.

	def visitAcao(self, ctx:fluxParser.AcaoContext, subgraphType = None):
		print("Action: " + ctx.STRING()[0].getText())
		if(subgraphType != None):
			print(f"Label: {subgraphType}")
		if(ctx.grafo() != None):
			if(ctx.STRING()[1] != None):
				self.visitGrafo(ctx.grafo(), ctx.STRING()[1].getText())
			else:
				self.visitGrafo(ctx.grafo(), None)
		return