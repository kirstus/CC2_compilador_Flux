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
		for graph in ctx.grafo():
			self.visitGrafo(graph)

	# Visit a parse tree produced by fluxParser#grafo.

	def visitGrafo(self, ctx:fluxParser.GrafoContext):
		for box in ctx.caixa():
			self.visitCaixa(box)
		if (ctx.retorno() != None):
			self.visitRetorno(ctx.retorno())


	# Visit a parse tree produced by fluxParser#caixa.

	def visitCaixa(self, ctx:fluxParser.CaixaContext):
		if (ctx.decisao() != None):
			self.visitDecisao(ctx.decisao())
		if (ctx.label() != None):
			self.visitLabel(ctx.label())
		if (ctx.loop() != None):
			self.visitLoop(ctx.loop())
		if (ctx.acao() != None):
			self.visitAcao(ctx.acao())

	# Visit a parse tree produced by fluxParser#decisao.

	def visitDecisao(self, ctx:fluxParser.DecisaoContext):
		if (ctx.cmdSe() != None):
			self.visitCmdSe(ctx.cmdSe())
		if (ctx.cmdSwitch() != None):
			self.visitCmdSwitch(ctx.cmdSwitch())

	# Visit a parse tree produced by fluxParser#retorno.

	def visitRetorno(self, ctx:fluxParser.RetornoContext):
		if(ctx.caixa() != None):
			self.visitCaixa(ctx.caixa())

	# Visit a parse tree produced by fluxParser#cmdSe.

	def visitCmdSe(self, ctx:fluxParser.CmdSeContext):
		self.visitCondicao(ctx.condicao())
		self.visitSubgrafo(ctx.subgrafo())
		if(ctx.cmdElse() != None):
			self.visitCmdElse(ctx.cmdElse())

	# Visit a parse tree produced by fluxParser#cmdElse.

	def visitCmdElse(self, ctx:fluxParser.CmdElseContext):
		self.visitSubgrafo(ctx.subgrafo())

	# Visit a parse tree produced by fluxParser#cmdSwitch.

	def visitCmdSwitch(self, ctx:fluxParser.CmdSwitchContext):
		self.visitCondicao(ctx.condicao())
		self.visitCasos(ctx.casos())

	# Visit a parse tree produced by fluxParser#casos.

	def visitCasos(self, ctx:fluxParser.CasosContext):
		for case in ctx.caso():
			self.visitCaso(case)
		if(ctx.implicacao() != None):
			self.visitImplicacao(ctx.implicacao()) 

	# Visit a parse tree produced by fluxParser#caso.

	def visitCaso(self, ctx:fluxParser.CasoContext):
		self.visitImplicacao(ctx.implicacao())

	# Visit a parse tree produced by fluxParser#implicacao.

	def visitImplicacao(self, ctx:fluxParser.ImplicacaoContext):
		self.visitSubgrafo(ctx.subgrafo())

	# Visit a parse tree produced by fluxParser#condicao.

	def visitCondicao(self, ctx:fluxParser.CondicaoContext):
		print(ctx.getText())

	# Visit a parse tree produced by fluxParser#subgrafo.

	def visitSubgrafo(self, ctx:fluxParser.SubgrafoContext):
		self.visitGrafo(ctx.grafo())

	# Visit a parse tree produced by fluxParser#label.

	def visitLabel(self, ctx:fluxParser.LabelContext):
		print(ctx.getText())

	# Visit a parse tree produced by fluxParser#loop.

	def visitLoop(self, ctx:fluxParser.LoopContext):
		print(ctx.getText())

	# Visit a parse tree produced by fluxParser#acao.

	def visitAcao(self, ctx:fluxParser.AcaoContext):
		print(ctx.getText())