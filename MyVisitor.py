__author__ = 'Santiago'

import importlib
import numpy as np
from antlr4 import *
from GDV_GrammarVisitor import GDV_GrammarVisitor
from GDV_GrammarParser import GDV_GrammarParser
from GDV_GrammarLexer import GDV_GrammarLexer
from typing import Callable, Dict, Union, Any
from importlib.machinery import SourceFileLoader
from error_manager import MyErrorListener, MyErrorStrategy

#Esta clase hereda de GDV_GrammarVisitor.py e implementa la funcionalidad que debe ejecutar el programa cuando se encuentre con cualquier
#no terminal del programa.

class MyVisitor(GDV_GrammarVisitor):
    def delete(self, X: str) -> None:
        try:
            del self.variablesDict[X]
        except:
            try:
                del self.functionsDict[X]
            except:
                raise Exception(f"la variable <{X}> no existe.")    


    def __init__(self):
        np.set_printoptions(suppress=True)
        self.variablesDict : Dict[str, Any] = {}
        self.functionsDict : Dict[str, Union[Callable, None]] = {
            "standard_out"       : print,
            "standard_in"        : input,
            "type"               : type,
            "length"             : len,
            "to_int"             : int,
            "to_float"           : float,
            "to_str"             : str,
            "to_bool"            : bool,
            "delete"             : self.delete
        }
        self.retorno = [False, None]

    def visitIf_stat(self, ctx):
        for i in range(len(ctx.condition_block())):
            if self.visit(ctx.condition_block(i).expr()):
                self.visit(ctx.condition_block(i))
                return
        try:                 
            if ctx.ELSE:
                self.visit(ctx.stat_block())
        except:
            return                

    def visitWhile_stat(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.stat_block())

    def visitFor_stat(self, ctx):
        self.visit(ctx.simple_stat(0))
        while self.visit(ctx.simple_stat(1).getChild(0)):
            self.visit(ctx.stat_block())
            self.visit(ctx.getChild(4))            


    def visitCondition_block(self, ctx):
        if self.visit(ctx.expr()):
            self.visit(ctx.stat_block())
            return

    def visitStat_block(self, ctx):
        for i in range(len(ctx.stat())):
            self.visit(ctx.stat(i))

    def visitFuncion(self, ctx):
        argo = []
        for i in range(len(ctx.parametro())):
            argo.append(ctx.parametro(i).getText())
        

        def f(*args):
            for ip, arg in enumerate(args):
                self.variablesDict[argo[ip]] = arg
            for ip in range(len((ctx.stat()))):
                self.visit(ctx.stat(ip))
                if self.retorno[0]:
                    valor = self.retorno[1]
                    self.retorno = [False, None] 
                    for ip, _ in enumerate(args):
                        del self.variablesDict[argo[ip]]   
                    return valor
            for ip, _ in enumerate(args):
                del self.variablesDict[argo[ip]]   
               
        self.functionsDict[ctx.ID().getText()] = f

    def visitAssignment(self, ctx):
        try:
            name = ctx.variable().getText()
            value = self.visit(ctx.expr())
            self.variablesDict[name] = value
        except:
            name = ctx.accessarray().variable().getText()
            value = self.visit(ctx.expr())
            indices = [self.visit(ctx.accessarray().expr(i)) for i in range(len(ctx.accessarray().expr()))]
            indices = tuple(indices)
            self.variablesDict[name][indices] = value

        return value

    def visitImportar(self, ctx):
        file_name = ctx.ID(0).getText()
        try:
            if ctx.ID(1).getText() == 'GDV':
                try:
                    input_stream1 = FileStream('/home/santiago/Documentos/lenguajes/GDVektor/lib/local/'+file_name+'.GDV')
                except:
                    input_stream1 = FileStream(file_name+'.GDV')
                lexer1 = GDV_GrammarLexer(input_stream1)
                lexer1.removeErrorListeners()
                lexer1._listeners = [ MyErrorListener() ]
                tokens1 = CommonTokenStream(lexer1)
                parser1 = GDV_GrammarParser(tokens1)
                parser1._listeners = [ MyErrorListener() ]
                parser1._errHandler = MyErrorStrategy()
                AUXtree = parser1.parse()
                self.visit(AUXtree)
            else:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}> El archivo {file_name} no tiene una extensión compatible.")                              
        except:    
            foo = SourceFileLoader(
                file_name,
                "/home/santiago/Documentos/lenguajes/GDVektor/lib/standard/" + file_name + "/" + file_name + ".py"
                ).load_module()
            module_members = dir(foo)
            for member_name in module_members:
                member = getattr(foo, member_name)
                if member_name[:2] != "__":
                    if callable(member):
                        self.functionsDict[member_name] = member
                    else:
                        self.variablesDict[member_name] = member

    def visitRetornar(self, ctx):
        self.retorno = [True, self.visit(ctx.expr())]

    def visitPowExpr(self, ctx):
        try:
            return self.visit(ctx.left) ** self.visit(ctx.left)
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '^'")
    
    def visitUnaryMinusExpr(self, ctx):
        return -(self.visit(ctx.expr()))

    def visitNotExpr(self, ctx):
        return not (self.visit(ctx.expr()))

    def visitMultiplicationExpr(self, ctx):
        if ctx.op.type == GDV_GrammarParser.MULT:
            try:
                return self.visit(ctx.left) * self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '*'")
        elif ctx.op.type == GDV_GrammarParser.DIV:
            try:
                return self.visit(ctx.left) / self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '/'")        
        else:
            try:
                return self.visit(ctx.left) % self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '%'")

    def visitAdditiveExpr(self, ctx):
        if ctx.op.type == GDV_GrammarParser.PLUS:
            try:
                return self.visit(ctx.left) + self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '+'")        
        else:
            try:
                return self.visit(ctx.left) - self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '-'")

    def visitRelationalExpr(self, ctx):
        if ctx.op.type == GDV_GrammarParser.LT:
            try:
                return self.visit(ctx.left) < self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '<'")
        elif ctx.op.type == GDV_GrammarParser.GT:
            try:
                return self.visit(ctx.left) > self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '>'")        
        elif ctx.op.type == GDV_GrammarParser.GTEQ:
            try:
                return self.visit(ctx.left) >= self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '>='")        
        else:
            try:
                return self.visit(ctx.left) <= self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '<='")

    def visitEqualityExpr(self, ctx):
        if ctx.op.type == GDV_GrammarParser.EQ:
            try:
                return self.visit(ctx.left) == self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '=='")        
        else:
            try:
                return self.visit(ctx.left) != self.visit(ctx.right)
            except:
                raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador '!='")

    def visitAndExpr(self, ctx):
        try:
            return self.visit(ctx.left) and self.visit(ctx.right)
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador 'and'")        

    def visitOrExpr(self, ctx):
        try:
            return self.visit(ctx.left) or self.visit(ctx.right)
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Una de las expresiones no es un tipo válido para el operador 'or'")        

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNumberAtom(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())        
        return float(ctx.FLOAT().getText())

    def visitBooleanAtom(self, ctx):
        if ctx.TRUE():
            return True        
        return False

    def visitFunccallAtom(self, ctx):
        return self.visit(ctx.funccall());                                  

    def visitStringAtom(self, ctx):
        string = str(ctx.STRING().getText())
        string = string[1:len(string) - 1]
        return string

    def visitArrayAtom(self, ctx):
        return self.visit(ctx.array())

    def visitObjetoAtom(self, ctx):
        return self.visit(ctx.objeto())

    def visitFunccall(self, ctx):
        try: 
            f = self.functionsDict[ctx.ID().getText()]
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: La función <{ctx.ID().getText()}> no ha sido declarada.")                            
    
        try:
            argumentos = []
            if ctx.expr():
                contador = 0
                while True:
                    try: 
                        argumentos.append(self.visit(ctx.expr(contador)))
                        contador+=1
                    except:
                        break
                return f(*argumentos)
            return f()

        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: La función <{ctx.ID().getText()}> toma un número diferente de argumentos o los argumentos no son válidos.")                                        


    def visitArray(self, ctx: GDV_GrammarParser.ArrayAtomContext):
        try:
            argumentos = []
            if ctx.expr():
                contador = 0
                while True:
                    try: 
                        argumentos.append(self.visit(ctx.expr(contador)))
                        contador+=1
                    except:
                        break
            return np.array(argumentos)
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: No se pudo convertir a un vector")   

    def visitAccessVariable(self, ctx):
        try:
            v = self.variablesDict[ctx.variable().ID(0).getText()]
            if len(ctx.variable().ID(0).getText()) > 1:
                for i in range(1, len(ctx.variable().ID())):
                    v = getattr(v,ctx.variable().ID(i).getText())
                    if callable(v):
                        argumentos = []
                        try:     
                            if ctx.getChild(0).expr():
                                for i in range(len(ctx.getChild(0).expr())):
                                    argumentos.append(self.visit(ctx.getChild(0).expr(i)))
                        except:
                            pass                                      
                        v = v(*argumentos)
            return v
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: La variable <{ctx.ID().getText()}> no ha sido declarada.")                                        

    def visitAccessToarray(self, ctx):
        try:
            v = self.variablesDict[ctx.getChild(0).getChild(0).getText()]

            for i in range(len(ctx.accessarray().expr())):
                v = v[self.visit(ctx.accessarray().expr(i))]
            return v
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: Índice o valor no accesible")                                                       
    def visitNilAtom(self, ctx):
        return None        

    def visitObjeto(self, ctx):
        try:
            argumentos = {}
            if ctx.keyvalue():
                contador = 0
                while True:
                    try: 
                        argumentos[ctx.keyvalue(contador).variable().getText()] = self.visit(ctx.keyvalue(contador).expr()) 
                        contador+=1
                    except:
                        break
            return argumentos
        except:
            raise Exception(f"<{ctx.start.line},{ctx.start.column}>Error semántico: No se pudo convertir a un diccionario")
