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
        4,1,17,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,3,2,33,8,2,1,2,1,2,1,3,1,3,3,3,39,8,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,70,8,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,84,8,7,10,7,12,7,87,9,7,
        1,8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,1,8,1,9,1,9,1,9,
        1,9,5,9,104,8,9,10,9,12,9,107,9,9,1,9,1,9,1,9,0,1,14,10,0,2,4,6,
        8,10,12,14,16,18,0,0,114,0,20,1,0,0,0,2,26,1,0,0,0,4,32,1,0,0,0,
        6,38,1,0,0,0,8,43,1,0,0,0,10,48,1,0,0,0,12,53,1,0,0,0,14,69,1,0,
        0,0,16,88,1,0,0,0,18,99,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,1,22,1,
        1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,
        26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,0,29,33,3,8,4,0,30,33,3,6,
        3,0,31,33,3,10,5,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        34,1,0,0,0,34,35,5,12,0,0,35,5,1,0,0,0,36,39,5,14,0,0,37,39,3,12,
        6,0,38,36,1,0,0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,41,5,11,0,0,41,
        42,3,14,7,0,42,7,1,0,0,0,43,44,5,3,0,0,44,45,5,15,0,0,45,46,3,14,
        7,0,46,47,5,16,0,0,47,9,1,0,0,0,48,49,5,4,0,0,49,50,5,15,0,0,50,
        51,5,14,0,0,51,52,5,16,0,0,52,11,1,0,0,0,53,54,5,14,0,0,54,55,5,
        1,0,0,55,56,5,5,0,0,56,57,5,13,0,0,57,58,5,5,0,0,58,59,5,2,0,0,59,
        13,1,0,0,0,60,61,6,7,-1,0,61,70,5,5,0,0,62,70,5,6,0,0,63,70,5,14,
        0,0,64,65,5,15,0,0,65,66,3,14,7,0,66,67,5,16,0,0,67,70,1,0,0,0,68,
        70,3,18,9,0,69,60,1,0,0,0,69,62,1,0,0,0,69,63,1,0,0,0,69,64,1,0,
        0,0,69,68,1,0,0,0,70,85,1,0,0,0,71,72,10,9,0,0,72,73,5,7,0,0,73,
        84,3,14,7,10,74,75,10,8,0,0,75,76,5,8,0,0,76,84,3,14,7,9,77,78,10,
        7,0,0,78,79,5,9,0,0,79,84,3,14,7,8,80,81,10,6,0,0,81,82,5,10,0,0,
        82,84,3,14,7,7,83,71,1,0,0,0,83,74,1,0,0,0,83,77,1,0,0,0,83,80,1,
        0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,0,87,
        85,1,0,0,0,88,89,5,1,0,0,89,94,5,5,0,0,90,91,5,13,0,0,91,93,5,5,
        0,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,
        1,0,0,0,96,94,1,0,0,0,97,98,5,2,0,0,98,17,1,0,0,0,99,100,5,1,0,0,
        100,105,3,16,8,0,101,102,5,13,0,0,102,104,3,16,8,0,103,101,1,0,0,
        0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,
        0,107,105,1,0,0,0,108,109,5,2,0,0,109,19,1,0,0,0,8,26,32,38,69,83,
        85,94,105
    ]

class MY_LANGParser ( Parser ):

    grammarFileName = "MY_LANG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'PRINT'", "'READ'", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'='", "';'", 
                     "','", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PRINT", "READ", 
                      "INT", "REAL", "MUL", "DIV", "ADD", "SUB", "SET", 
                      "EOE", "COMA", "ID", "LEFT_P", "RIGHT_P", "WS" ]

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

    ruleNames =  [ "prog", "statements", "statement", "assign", "print", 
                   "read", "matrix_elem", "expr", "row", "matrix" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PRINT=3
    READ=4
    INT=5
    REAL=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    SET=11
    EOE=12
    COMA=13
    ID=14
    LEFT_P=15
    RIGHT_P=16
    WS=17

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
            self.state = 20
            self.statements()
            self.state = 21
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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16408) != 0):
                self.state = 23
                self.statement()
                self.state = 28
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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 29
                self.print_()
                pass
            elif token in [14]:
                self.state = 30
                self.assign()
                pass
            elif token in [4]:
                self.state = 31
                self.read()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 34
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(MY_LANGParser.ID)
                pass

            elif la_ == 2:
                self.state = 37
                self.matrix_elem()
                pass


            self.state = 40
            self.match(MY_LANGParser.SET)
            self.state = 41
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
            self.state = 43
            self.match(MY_LANGParser.PRINT)
            self.state = 44
            self.match(MY_LANGParser.LEFT_P)
            self.state = 45
            self.expr(0)
            self.state = 46
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
            self.state = 48
            self.match(MY_LANGParser.READ)
            self.state = 49
            self.match(MY_LANGParser.LEFT_P)
            self.state = 50
            self.match(MY_LANGParser.ID)
            self.state = 51
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
            self.state = 53
            self.match(MY_LANGParser.ID)
            self.state = 54
            self.match(MY_LANGParser.T__0)
            self.state = 55
            self.match(MY_LANGParser.INT)
            self.state = 56
            self.match(MY_LANGParser.COMA)
            self.state = 57
            self.match(MY_LANGParser.INT)
            self.state = 58
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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 61
                self.match(MY_LANGParser.INT)
                pass
            elif token in [6]:
                self.state = 62
                self.match(MY_LANGParser.REAL)
                pass
            elif token in [14]:
                self.state = 63
                self.match(MY_LANGParser.ID)
                pass
            elif token in [15]:
                self.state = 64
                self.match(MY_LANGParser.LEFT_P)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(MY_LANGParser.RIGHT_P)
                pass
            elif token in [1]:
                self.state = 68
                self.matrix()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 72
                        self.match(MY_LANGParser.MUL)
                        self.state = 73
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 75
                        self.match(MY_LANGParser.DIV)
                        self.state = 76
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 78
                        self.match(MY_LANGParser.ADD)
                        self.state = 79
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 81
                        self.match(MY_LANGParser.SUB)
                        self.state = 82
                        self.expr(7)
                        pass

             
                self.state = 87
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
            self.state = 88
            self.match(MY_LANGParser.T__0)
            self.state = 89
            self.match(MY_LANGParser.INT)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 90
                self.match(MY_LANGParser.COMA)
                self.state = 91
                self.match(MY_LANGParser.INT)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
            self.match(MY_LANGParser.T__0)
            self.state = 100
            self.row()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 101
                self.match(MY_LANGParser.COMA)
                self.state = 102
                self.row()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(MY_LANGParser.T__1)
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
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




