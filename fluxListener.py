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


    # Enter a parse tree produced by fluxParser#decisão.
    def enterDecisão(self, ctx:fluxParser.DecisãoContext):
        pass

    # Exit a parse tree produced by fluxParser#decisão.
    def exitDecisão(self, ctx:fluxParser.DecisãoContext):
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


    # Enter a parse tree produced by fluxParser#implicação.
    def enterImplicação(self, ctx:fluxParser.ImplicaçãoContext):
        pass

    # Exit a parse tree produced by fluxParser#implicação.
    def exitImplicação(self, ctx:fluxParser.ImplicaçãoContext):
        pass


    # Enter a parse tree produced by fluxParser#condição.
    def enterCondição(self, ctx:fluxParser.CondiçãoContext):
        pass

    # Exit a parse tree produced by fluxParser#condição.
    def exitCondição(self, ctx:fluxParser.CondiçãoContext):
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


    # Enter a parse tree produced by fluxParser#ação.
    def enterAção(self, ctx:fluxParser.AçãoContext):
        pass

    # Exit a parse tree produced by fluxParser#ação.
    def exitAção(self, ctx:fluxParser.AçãoContext):
        pass


