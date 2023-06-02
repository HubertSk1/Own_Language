# Generated from MY_LANG.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,5,1,27,8,1,10,
        1,12,1,30,9,1,1,2,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,3,1,3,3,3,42,
        8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        74,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,88,8,
        7,10,7,12,7,91,9,7,1,8,1,8,1,8,1,8,5,8,97,8,8,10,8,12,8,100,9,8,
        1,8,1,8,1,9,1,9,1,9,1,9,5,9,108,8,9,10,9,12,9,111,9,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,0,1,14,11,0,2,4,6,8,10,12,
        14,16,18,20,0,0,126,0,22,1,0,0,0,2,28,1,0,0,0,4,35,1,0,0,0,6,41,
        1,0,0,0,8,46,1,0,0,0,10,51,1,0,0,0,12,56,1,0,0,0,14,73,1,0,0,0,16,
        92,1,0,0,0,18,103,1,0,0,0,20,114,1,0,0,0,22,23,3,2,1,0,23,24,5,0,
        0,1,24,1,1,0,0,0,25,27,3,4,2,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,
        1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,28,1,0,0,0,31,36,3,8,4,0,32,
        36,3,6,3,0,33,36,3,10,5,0,34,36,3,20,10,0,35,31,1,0,0,0,35,32,1,
        0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,38,5,13,0,0,38,
        5,1,0,0,0,39,42,5,15,0,0,40,42,3,12,6,0,41,39,1,0,0,0,41,40,1,0,
        0,0,42,43,1,0,0,0,43,44,5,12,0,0,44,45,3,14,7,0,45,7,1,0,0,0,46,
        47,5,4,0,0,47,48,5,16,0,0,48,49,3,14,7,0,49,50,5,17,0,0,50,9,1,0,
        0,0,51,52,5,5,0,0,52,53,5,16,0,0,53,54,5,15,0,0,54,55,5,17,0,0,55,
        11,1,0,0,0,56,57,5,15,0,0,57,58,5,1,0,0,58,59,5,6,0,0,59,60,5,14,
        0,0,60,61,5,6,0,0,61,62,5,2,0,0,62,13,1,0,0,0,63,64,6,7,-1,0,64,
        74,5,6,0,0,65,74,5,7,0,0,66,74,5,15,0,0,67,68,5,16,0,0,68,69,3,14,
        7,0,69,70,5,17,0,0,70,74,1,0,0,0,71,74,3,18,9,0,72,74,3,12,6,0,73,
        63,1,0,0,0,73,65,1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,71,1,0,0,
        0,73,72,1,0,0,0,74,89,1,0,0,0,75,76,10,10,0,0,76,77,5,8,0,0,77,88,
        3,14,7,11,78,79,10,9,0,0,79,80,5,9,0,0,80,88,3,14,7,10,81,82,10,
        8,0,0,82,83,5,10,0,0,83,88,3,14,7,9,84,85,10,7,0,0,85,86,5,11,0,
        0,86,88,3,14,7,8,87,75,1,0,0,0,87,78,1,0,0,0,87,81,1,0,0,0,87,84,
        1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,15,1,0,0,0,
        91,89,1,0,0,0,92,93,5,1,0,0,93,98,5,6,0,0,94,95,5,14,0,0,95,97,5,
        6,0,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,
        101,1,0,0,0,100,98,1,0,0,0,101,102,5,2,0,0,102,17,1,0,0,0,103,104,
        5,1,0,0,104,109,3,16,8,0,105,106,5,14,0,0,106,108,3,16,8,0,107,105,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,
        1,0,0,0,111,109,1,0,0,0,112,113,5,2,0,0,113,19,1,0,0,0,114,115,5,
        3,0,0,115,116,5,16,0,0,116,117,5,15,0,0,117,118,5,14,0,0,118,119,
        5,6,0,0,119,120,5,17,0,0,120,21,1,0,0,0,8,28,35,41,73,87,89,98,109
    ]

class MY_LANGParser ( Parser ):

    grammarFileName = "MY_LANG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'SCALE'", "'PRINT'", "'READ'", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'+'", "'-'", 
                     "'='", "';'", "','", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SCALE", "PRINT", 
                      "READ", "INT", "REAL", "MUL", "DIV", "ADD", "SUB", 
                      "SET", "EOE", "COMA", "ID", "LEFT_P", "RIGHT_P", "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_assign = 3
    RULE_print = 4
    RULE_read = 5
    RULE_matrix_elem = 6
    RULE_expr = 7
    RULE_row = 8
    RULE_matrix = 9
    RULE_scale = 10

    ruleNames =  [ "prog", "statements", "statement", "assign", "print", 
                   "read", "matrix_elem", "expr", "row", "matrix", "scale" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SCALE=3
    PRINT=4
    READ=5
    INT=6
    REAL=7
    MUL=8
    DIV=9
    ADD=10
    SUB=11
    SET=12
    EOE=13
    COMA=14
    ID=15
    LEFT_P=16
    RIGHT_P=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(MY_LANGParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(MY_LANGParser.EOF, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MY_LANGParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.statements()
            self.state = 23
            self.match(MY_LANGParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.StatementContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.StatementContext,i)


        def getRuleIndex(self):
            return MY_LANGParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MY_LANGParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32824) != 0):
                self.state = 25
                self.statement()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOE(self):
            return self.getToken(MY_LANGParser.EOE, 0)

        def print_(self):
            return self.getTypedRuleContext(MY_LANGParser.PrintContext,0)


        def assign(self):
            return self.getTypedRuleContext(MY_LANGParser.AssignContext,0)


        def read(self):
            return self.getTypedRuleContext(MY_LANGParser.ReadContext,0)


        def scale(self):
            return self.getTypedRuleContext(MY_LANGParser.ScaleContext,0)


        def getRuleIndex(self):
            return MY_LANGParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MY_LANGParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 31
                self.print_()
                pass
            elif token in [15]:
                self.state = 32
                self.assign()
                pass
            elif token in [5]:
                self.state = 33
                self.read()
                pass
            elif token in [3]:
                self.state = 34
                self.scale()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 37
            self.match(MY_LANGParser.EOE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(MY_LANGParser.SET, 0)

        def expr(self):
            return self.getTypedRuleContext(MY_LANGParser.ExprContext,0)


        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def matrix_elem(self):
            return self.getTypedRuleContext(MY_LANGParser.Matrix_elemContext,0)


        def getRuleIndex(self):
            return MY_LANGParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = MY_LANGParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 39
                self.match(MY_LANGParser.ID)
                pass

            elif la_ == 2:
                self.state = 40
                self.matrix_elem()
                pass


            self.state = 43
            self.match(MY_LANGParser.SET)
            self.state = 44
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MY_LANGParser.PRINT, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def expr(self):
            return self.getTypedRuleContext(MY_LANGParser.ExprContext,0)


        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = MY_LANGParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MY_LANGParser.PRINT)
            self.state = 47
            self.match(MY_LANGParser.LEFT_P)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(MY_LANGParser.READ, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = MY_LANGParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MY_LANGParser.READ)
            self.state = 52
            self.match(MY_LANGParser.LEFT_P)
            self.state = 53
            self.match(MY_LANGParser.ID)
            self.state = 54
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.INT)
            else:
                return self.getToken(MY_LANGParser.INT, i)

        def COMA(self):
            return self.getToken(MY_LANGParser.COMA, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_matrix_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_elem" ):
                listener.enterMatrix_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_elem" ):
                listener.exitMatrix_elem(self)




    def matrix_elem(self):

        localctx = MY_LANGParser.Matrix_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matrix_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MY_LANGParser.ID)
            self.state = 57
            self.match(MY_LANGParser.T__0)
            self.state = 58
            self.match(MY_LANGParser.INT)
            self.state = 59
            self.match(MY_LANGParser.COMA)
            self.state = 60
            self.match(MY_LANGParser.INT)
            self.state = 61
            self.match(MY_LANGParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MY_LANGParser.INT, 0)

        def REAL(self):
            return self.getToken(MY_LANGParser.REAL, 0)

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.ExprContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.ExprContext,i)


        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def matrix(self):
            return self.getTypedRuleContext(MY_LANGParser.MatrixContext,0)


        def matrix_elem(self):
            return self.getTypedRuleContext(MY_LANGParser.Matrix_elemContext,0)


        def MUL(self):
            return self.getToken(MY_LANGParser.MUL, 0)

        def DIV(self):
            return self.getToken(MY_LANGParser.DIV, 0)

        def ADD(self):
            return self.getToken(MY_LANGParser.ADD, 0)

        def SUB(self):
            return self.getToken(MY_LANGParser.SUB, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MY_LANGParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(MY_LANGParser.INT)
                pass

            elif la_ == 2:
                self.state = 65
                self.match(MY_LANGParser.REAL)
                pass

            elif la_ == 3:
                self.state = 66
                self.match(MY_LANGParser.ID)
                pass

            elif la_ == 4:
                self.state = 67
                self.match(MY_LANGParser.LEFT_P)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(MY_LANGParser.RIGHT_P)
                pass

            elif la_ == 5:
                self.state = 71
                self.matrix()
                pass

            elif la_ == 6:
                self.state = 72
                self.matrix_elem()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 76
                        self.match(MY_LANGParser.MUL)
                        self.state = 77
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 79
                        self.match(MY_LANGParser.DIV)
                        self.state = 80
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 82
                        self.match(MY_LANGParser.ADD)
                        self.state = 83
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 85
                        self.match(MY_LANGParser.SUB)
                        self.state = 86
                        self.expr(8)
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.INT)
            else:
                return self.getToken(MY_LANGParser.INT, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.COMA)
            else:
                return self.getToken(MY_LANGParser.COMA, i)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = MY_LANGParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MY_LANGParser.T__0)
            self.state = 93
            self.match(MY_LANGParser.INT)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 94
                self.match(MY_LANGParser.COMA)
                self.state = 95
                self.match(MY_LANGParser.INT)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(MY_LANGParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.RowContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.RowContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.COMA)
            else:
                return self.getToken(MY_LANGParser.COMA, i)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)




    def matrix(self):

        localctx = MY_LANGParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(MY_LANGParser.T__0)
            self.state = 104
            self.row()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 105
                self.match(MY_LANGParser.COMA)
                self.state = 106
                self.row()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(MY_LANGParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScaleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCALE(self):
            return self.getToken(MY_LANGParser.SCALE, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def COMA(self):
            return self.getToken(MY_LANGParser.COMA, 0)

        def INT(self):
            return self.getToken(MY_LANGParser.INT, 0)

        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_scale

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScale" ):
                listener.enterScale(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScale" ):
                listener.exitScale(self)




    def scale(self):

        localctx = MY_LANGParser.ScaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MY_LANGParser.SCALE)
            self.state = 115
            self.match(MY_LANGParser.LEFT_P)
            self.state = 116
            self.match(MY_LANGParser.ID)
            self.state = 117
            self.match(MY_LANGParser.COMA)
            self.state = 118
            self.match(MY_LANGParser.INT)
            self.state = 119
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         




