# Generated from flux.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fluxParser import fluxParser
else:
    from fluxParser import fluxParser

# This class defines a complete listener for a parse tree produced by fluxParser.
class fluxListener(ParseTreeListener):

    # Enter a parse tree produced by fluxParser#fluxograma.
    def enterFluxograma(self, ctx:fluxParser.FluxogramaContext):
        pass

    # Exit a parse tree produced by fluxParser#fluxograma.
    def exitFluxograma(self, ctx:fluxParser.FluxogramaContext):
        pass


    # Enter a parse tree produced by fluxParser#grafo.
    def enterGrafo(self, ctx:fluxParser.GrafoContext):
        pass

    # Exit a parse tree produced by fluxParser#grafo.
    def exitGrafo(self, ctx:fluxParser.GrafoContext):
        pass


    # Enter a parse tree produced by fluxParser#caixa.
    def enterCaixa(self, ctx:fluxParser.CaixaContext):
        pass

    # Exit a parse tree produced by fluxParser#caixa.
    def exitCaixa(self, ctx:fluxParser.CaixaContext):
        pass


    # Enter a parse tree produced by fluxParser#decisao.
    def enterDecisao(self, ctx:fluxParser.DecisaoContext):
        pass

    # Exit a parse tree produced by fluxParser#decisao.
    def exitDecisao(self, ctx:fluxParser.DecisaoContext):
        pass


    # Enter a parse tree produced by fluxParser#retorno.
    def enterRetorno(self, ctx:fluxParser.RetornoContext):
        pass

    # Exit a parse tree produced by fluxParser#retorno.
    def exitRetorno(self, ctx:fluxParser.RetornoContext):
        pass


    # Enter a parse tree produced by fluxParser#cmdSe.
    def enterCmdSe(self, ctx:fluxParser.CmdSeContext):
        pass

    # Exit a parse tree produced by fluxParser#cmdSe.
    def exitCmdSe(self, ctx:fluxParser.CmdSeContext):
        pass


    # Enter a parse tree produced by fluxParser#cmdElse.
    def enterCmdElse(self, ctx:fluxParser.CmdElseContext):
        pass

    # Exit a parse tree produced by fluxParser#cmdElse.
    def exitCmdElse(self, ctx:fluxParser.CmdElseContext):
        pass


    # Enter a parse tree produced by fluxParser#cmdSwitch.
    def enterCmdSwitch(self, ctx:fluxParser.CmdSwitchContext):
        pass

    # Exit a parse tree produced by fluxParser#cmdSwitch.
    def exitCmdSwitch(self, ctx:fluxParser.CmdSwitchContext):
        pass


    # Enter a parse tree produced by fluxParser#casos.
    def enterCasos(self, ctx:fluxParser.CasosContext):
        pass

    # Exit a parse tree produced by fluxParser#casos.
    def exitCasos(self, ctx:fluxParser.CasosContext):
        pass


    # Enter a parse tree produced by fluxParser#caso.
    def enterCaso(self, ctx:fluxParser.CasoContext):
        pass

    # Exit a parse tree produced by fluxParser#caso.
    def exitCaso(self, ctx:fluxParser.CasoContext):
        pass


    # Enter a parse tree produced by fluxParser#implicacao.
    def enterImplicacao(self, ctx:fluxParser.ImplicacaoContext):
        pass

    # Exit a parse tree produced by fluxParser#implicacao.
    def exitImplicacao(self, ctx:fluxParser.ImplicacaoContext):
        pass


    # Enter a parse tree produced by fluxParser#condicao.
    def enterCondicao(self, ctx:fluxParser.CondicaoContext):
        pass

    # Exit a parse tree produced by fluxParser#condicao.
    def exitCondicao(self, ctx:fluxParser.CondicaoContext):
        pass


    # Enter a parse tree produced by fluxParser#subgrafo.
    def enterSubgrafo(self, ctx:fluxParser.SubgrafoContext):
        pass

    # Exit a parse tree produced by fluxParser#subgrafo.
    def exitSubgrafo(self, ctx:fluxParser.SubgrafoContext):
        pass


    # Enter a parse tree produced by fluxParser#label.
    def enterLabel(self, ctx:fluxParser.LabelContext):
        pass

    # Exit a parse tree produced by fluxParser#label.
    def exitLabel(self, ctx:fluxParser.LabelContext):
        pass


    # Enter a parse tree produced by fluxParser#loop.
    def enterLoop(self, ctx:fluxParser.LoopContext):
        pass

    # Exit a parse tree produced by fluxParser#loop.
    def exitLoop(self, ctx:fluxParser.LoopContext):
        pass


    # Enter a parse tree produced by fluxParser#acao.
    def enterAcao(self, ctx:fluxParser.AcaoContext):
        pass

    # Exit a parse tree produced by fluxParser#acao.
    def exitAcao(self, ctx:fluxParser.AcaoContext):
        pass


