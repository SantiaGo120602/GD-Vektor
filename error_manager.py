from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *

class RetornoException(Exception):
    pass


class MyErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer:Parser, e:RecognitionException):
        recognizer._errHandler.reportError(recognizer,e)
        super().recover(recognizer,e)

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        symbol = str(offendingSymbol)
        errorsymbol = ""
        comas = 0
        for c in symbol:
            if c == "'":
                errorsymbol+=c
                comas+=1
            if comas ==1 and c!="'":
                errorsymbol+=c

        symbol = str(msg)
        añadir = False
        correcSymbol = ""
        for i in range(len(symbol)):
            if añadir:
                correcSymbol+=symbol[i]
            if symbol[i] == " " and symbol[i-1] == "g":
                añadir = True

        print(f'<{line},{column}> Error sintáctico: Se encontró: {errorsymbol}. Se esperaba: {correcSymbol}')

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass