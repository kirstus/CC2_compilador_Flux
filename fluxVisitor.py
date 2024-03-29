# Generated from flux.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fluxParser import fluxParser
else:
    from fluxParser import fluxParser

# This class defines a complete generic visitor for a parse tree produced by fluxParser.

class fluxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fluxParser#fluxograma.
    def visitFluxograma(self, ctx:fluxParser.FluxogramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#grafo.
    def visitGrafo(self, ctx:fluxParser.GrafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#caixa.
    def visitCaixa(self, ctx:fluxParser.CaixaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#decisao.
    def visitDecisao(self, ctx:fluxParser.DecisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#retorno.
    def visitRetorno(self, ctx:fluxParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#cmdSe.
    def visitCmdSe(self, ctx:fluxParser.CmdSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#cmdElse.
    def visitCmdElse(self, ctx:fluxParser.CmdElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#cmdSwitch.
    def visitCmdSwitch(self, ctx:fluxParser.CmdSwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#casos.
    def visitCasos(self, ctx:fluxParser.CasosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#caso.
    def visitCaso(self, ctx:fluxParser.CasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#implicacao.
    def visitImplicacao(self, ctx:fluxParser.ImplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#condicao.
    def visitCondicao(self, ctx:fluxParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#subgrafo.
    def visitSubgrafo(self, ctx:fluxParser.SubgrafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#label.
    def visitLabel(self, ctx:fluxParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#loop.
    def visitLoop(self, ctx:fluxParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fluxParser#acao.
    def visitAcao(self, ctx:fluxParser.AcaoContext):
        return self.visitChildren(ctx)



del fluxParser