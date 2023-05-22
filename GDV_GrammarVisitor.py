# Generated from GDV_Grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GDV_GrammarParser import GDV_GrammarParser
else:
    from GDV_GrammarParser import GDV_GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GDV_GrammarParser.

class GDV_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GDV_GrammarParser#parse.
    def visitParse(self, ctx:GDV_GrammarParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#from_input.
    def visitFrom_input(self, ctx:GDV_GrammarParser.From_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#from_file.
    def visitFrom_file(self, ctx:GDV_GrammarParser.From_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#stat.
    def visitStat(self, ctx:GDV_GrammarParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#compound_stat.
    def visitCompound_stat(self, ctx:GDV_GrammarParser.Compound_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#simple_stat.
    def visitSimple_stat(self, ctx:GDV_GrammarParser.Simple_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#assignment.
    def visitAssignment(self, ctx:GDV_GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#if_stat.
    def visitIf_stat(self, ctx:GDV_GrammarParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#while_stat.
    def visitWhile_stat(self, ctx:GDV_GrammarParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#for_stat.
    def visitFor_stat(self, ctx:GDV_GrammarParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#funcion.
    def visitFuncion(self, ctx:GDV_GrammarParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#importar.
    def visitImportar(self, ctx:GDV_GrammarParser.ImportarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#retornar.
    def visitRetornar(self, ctx:GDV_GrammarParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#condition_block.
    def visitCondition_block(self, ctx:GDV_GrammarParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#stat_block.
    def visitStat_block(self, ctx:GDV_GrammarParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#array.
    def visitArray(self, ctx:GDV_GrammarParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#accessarray.
    def visitAccessarray(self, ctx:GDV_GrammarParser.AccessarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#variable.
    def visitVariable(self, ctx:GDV_GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#parametro.
    def visitParametro(self, ctx:GDV_GrammarParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#parExpr.
    def visitParExpr(self, ctx:GDV_GrammarParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#notExpr.
    def visitNotExpr(self, ctx:GDV_GrammarParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:GDV_GrammarParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:GDV_GrammarParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#atomExpr.
    def visitAtomExpr(self, ctx:GDV_GrammarParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#orExpr.
    def visitOrExpr(self, ctx:GDV_GrammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:GDV_GrammarParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#powExpr.
    def visitPowExpr(self, ctx:GDV_GrammarParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#relationalExpr.
    def visitRelationalExpr(self, ctx:GDV_GrammarParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#equalityExpr.
    def visitEqualityExpr(self, ctx:GDV_GrammarParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#andExpr.
    def visitAndExpr(self, ctx:GDV_GrammarParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#funccall.
    def visitFunccall(self, ctx:GDV_GrammarParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#numberAtom.
    def visitNumberAtom(self, ctx:GDV_GrammarParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#booleanAtom.
    def visitBooleanAtom(self, ctx:GDV_GrammarParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#funccallAtom.
    def visitFunccallAtom(self, ctx:GDV_GrammarParser.FunccallAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#stringAtom.
    def visitStringAtom(self, ctx:GDV_GrammarParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#arrayAtom.
    def visitArrayAtom(self, ctx:GDV_GrammarParser.ArrayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#objetoAtom.
    def visitObjetoAtom(self, ctx:GDV_GrammarParser.ObjetoAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#accessToarray.
    def visitAccessToarray(self, ctx:GDV_GrammarParser.AccessToarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#accessVariable.
    def visitAccessVariable(self, ctx:GDV_GrammarParser.AccessVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#nilAtom.
    def visitNilAtom(self, ctx:GDV_GrammarParser.NilAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#objeto.
    def visitObjeto(self, ctx:GDV_GrammarParser.ObjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GDV_GrammarParser#keyvalue.
    def visitKeyvalue(self, ctx:GDV_GrammarParser.KeyvalueContext):
        return self.visitChildren(ctx)



del GDV_GrammarParser