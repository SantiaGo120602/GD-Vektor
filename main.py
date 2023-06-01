__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.Errors import ParseCancellationException
from GDV_GrammarLexer import GDV_GrammarLexer
from GDV_GrammarParser import GDV_GrammarParser
from MyVisitor import MyVisitor
from error_manager import MyErrorListener, MyErrorStrategy


if __name__ == '__main__':
    

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    #Analizador léxico
    lexer = GDV_GrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer._listeners = [ MyErrorListener() ]
    token_stream = CommonTokenStream(lexer)
    #Analizador sintáctico
    parser = GDV_GrammarParser(token_stream)
    parser._listeners = [ MyErrorListener() ]
    parser._errHandler = MyErrorStrategy()
    try:
        #Generación del árbol de sintáxis abstracta
        tree = parser.parse()
        #Se visita el árbol de sintáxis abstracta con el programa MyVisitor
        visitor = MyVisitor()
        visitor.visit(tree)
    except ParseCancellationException:
        pass

