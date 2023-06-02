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
        4,1,20,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        42,8,2,1,2,1,2,1,3,1,3,3,3,48,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,5,9,110,8,9,10,9,12,9,113,9,9,1,10,1,10,1,10,
        1,10,5,10,119,8,10,10,10,12,10,122,9,10,1,10,1,10,1,11,1,11,1,11,
        1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,0,1,18,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,0,148,0,26,1,0,0,0,2,32,1,0,0,0,4,41,1,0,0,0,6,47,1,0,0,0,8,
        52,1,0,0,0,10,57,1,0,0,0,12,62,1,0,0,0,14,69,1,0,0,0,16,76,1,0,0,
        0,18,95,1,0,0,0,20,114,1,0,0,0,22,125,1,0,0,0,24,136,1,0,0,0,26,
        27,3,2,1,0,27,28,5,0,0,1,28,1,1,0,0,0,29,31,3,4,2,0,30,29,1,0,0,
        0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,1,0,0,0,34,32,1,
        0,0,0,35,42,3,8,4,0,36,42,3,6,3,0,37,42,3,10,5,0,38,42,3,24,12,0,
        39,42,3,12,6,0,40,42,3,16,8,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,
        1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,43,1,0,0,0,
        43,44,5,15,0,0,44,5,1,0,0,0,45,48,5,17,0,0,46,48,3,14,7,0,47,45,
        1,0,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,50,5,14,0,0,50,51,3,18,9,
        0,51,7,1,0,0,0,52,53,5,6,0,0,53,54,5,18,0,0,54,55,3,18,9,0,55,56,
        5,19,0,0,56,9,1,0,0,0,57,58,5,7,0,0,58,59,5,18,0,0,59,60,5,17,0,
        0,60,61,5,19,0,0,61,11,1,0,0,0,62,63,5,4,0,0,63,64,5,18,0,0,64,65,
        5,17,0,0,65,66,5,16,0,0,66,67,5,17,0,0,67,68,5,19,0,0,68,13,1,0,
        0,0,69,70,5,17,0,0,70,71,5,1,0,0,71,72,5,8,0,0,72,73,5,16,0,0,73,
        74,5,8,0,0,74,75,5,2,0,0,75,15,1,0,0,0,76,77,5,3,0,0,77,78,5,18,
        0,0,78,79,5,17,0,0,79,80,5,16,0,0,80,81,5,17,0,0,81,82,5,16,0,0,
        82,83,5,17,0,0,83,84,5,19,0,0,84,17,1,0,0,0,85,86,6,9,-1,0,86,96,
        5,8,0,0,87,96,5,9,0,0,88,96,5,17,0,0,89,90,5,18,0,0,90,91,3,18,9,
        0,91,92,5,19,0,0,92,96,1,0,0,0,93,96,3,22,11,0,94,96,3,14,7,0,95,
        85,1,0,0,0,95,87,1,0,0,0,95,88,1,0,0,0,95,89,1,0,0,0,95,93,1,0,0,
        0,95,94,1,0,0,0,96,111,1,0,0,0,97,98,10,10,0,0,98,99,5,10,0,0,99,
        110,3,18,9,11,100,101,10,9,0,0,101,102,5,11,0,0,102,110,3,18,9,10,
        103,104,10,8,0,0,104,105,5,12,0,0,105,110,3,18,9,9,106,107,10,7,
        0,0,107,108,5,13,0,0,108,110,3,18,9,8,109,97,1,0,0,0,109,100,1,0,
        0,0,109,103,1,0,0,0,109,106,1,0,0,0,110,113,1,0,0,0,111,109,1,0,
        0,0,111,112,1,0,0,0,112,19,1,0,0,0,113,111,1,0,0,0,114,115,5,1,0,
        0,115,120,5,8,0,0,116,117,5,16,0,0,117,119,5,8,0,0,118,116,1,0,0,
        0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,
        0,122,120,1,0,0,0,123,124,5,2,0,0,124,21,1,0,0,0,125,126,5,1,0,0,
        126,131,3,20,10,0,127,128,5,16,0,0,128,130,3,20,10,0,129,127,1,0,
        0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,
        0,0,133,131,1,0,0,0,134,135,5,2,0,0,135,23,1,0,0,0,136,137,5,5,0,
        0,137,138,5,18,0,0,138,139,5,17,0,0,139,140,5,16,0,0,140,141,5,8,
        0,0,141,142,5,19,0,0,142,25,1,0,0,0,8,32,41,47,95,109,111,120,131
    ]

class MY_LANGParser ( Parser ):

    grammarFileName = "MY_LANG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'SIZE'", "'ADD'", "'SCALE'", 
                     "'PRINT'", "'READ'", "<INVALID>", "<INVALID>", "'*'", 
                     "'/'", "'+'", "'-'", "'='", "';'", "','", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "M_SIZE", "M_ADD", 
                      "SCALE", "PRINT", "READ", "INT", "REAL", "MUL", "DIV", 
                      "ADD", "SUB", "SET", "EOE", "COMA", "ID", "LEFT_P", 
                      "RIGHT_P", "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_assign = 3
    RULE_print = 4
    RULE_read = 5
    RULE_matrix_add = 6
    RULE_matrix_elem = 7
    RULE_matrix_size = 8
    RULE_expr = 9
    RULE_row = 10
    RULE_matrix = 11
    RULE_scale = 12

    ruleNames =  [ "prog", "statements", "statement", "assign", "print", 
                   "read", "matrix_add", "matrix_elem", "matrix_size", "expr", 
                   "row", "matrix", "scale" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    M_SIZE=3
    M_ADD=4
    SCALE=5
    PRINT=6
    READ=7
    INT=8
    REAL=9
    MUL=10
    DIV=11
    ADD=12
    SUB=13
    SET=14
    EOE=15
    COMA=16
    ID=17
    LEFT_P=18
    RIGHT_P=19
    WS=20

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
            self.state = 26
            self.statements()
            self.state = 27
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
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131320) != 0):
                self.state = 29
                self.statement()
                self.state = 34
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


        def matrix_add(self):
            return self.getTypedRuleContext(MY_LANGParser.Matrix_addContext,0)


        def matrix_size(self):
            return self.getTypedRuleContext(MY_LANGParser.Matrix_sizeContext,0)


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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 35
                self.print_()
                pass
            elif token in [17]:
                self.state = 36
                self.assign()
                pass
            elif token in [7]:
                self.state = 37
                self.read()
                pass
            elif token in [5]:
                self.state = 38
                self.scale()
                pass
            elif token in [4]:
                self.state = 39
                self.matrix_add()
                pass
            elif token in [3]:
                self.state = 40
                self.matrix_size()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 43
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 45
                self.match(MY_LANGParser.ID)
                pass

            elif la_ == 2:
                self.state = 46
                self.matrix_elem()
                pass


            self.state = 49
            self.match(MY_LANGParser.SET)
            self.state = 50
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
            self.state = 52
            self.match(MY_LANGParser.PRINT)
            self.state = 53
            self.match(MY_LANGParser.LEFT_P)
            self.state = 54
            self.expr(0)
            self.state = 55
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
            self.state = 57
            self.match(MY_LANGParser.READ)
            self.state = 58
            self.match(MY_LANGParser.LEFT_P)
            self.state = 59
            self.match(MY_LANGParser.ID)
            self.state = 60
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def M_ADD(self):
            return self.getToken(MY_LANGParser.M_ADD, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.ID)
            else:
                return self.getToken(MY_LANGParser.ID, i)

        def COMA(self):
            return self.getToken(MY_LANGParser.COMA, 0)

        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_matrix_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_add" ):
                listener.enterMatrix_add(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_add" ):
                listener.exitMatrix_add(self)




    def matrix_add(self):

        localctx = MY_LANGParser.Matrix_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matrix_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MY_LANGParser.M_ADD)
            self.state = 63
            self.match(MY_LANGParser.LEFT_P)
            self.state = 64
            self.match(MY_LANGParser.ID)
            self.state = 65
            self.match(MY_LANGParser.COMA)
            self.state = 66
            self.match(MY_LANGParser.ID)
            self.state = 67
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
        self.enterRule(localctx, 14, self.RULE_matrix_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MY_LANGParser.ID)
            self.state = 70
            self.match(MY_LANGParser.T__0)
            self.state = 71
            self.match(MY_LANGParser.INT)
            self.state = 72
            self.match(MY_LANGParser.COMA)
            self.state = 73
            self.match(MY_LANGParser.INT)
            self.state = 74
            self.match(MY_LANGParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def M_SIZE(self):
            return self.getToken(MY_LANGParser.M_SIZE, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.ID)
            else:
                return self.getToken(MY_LANGParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.COMA)
            else:
                return self.getToken(MY_LANGParser.COMA, i)

        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_matrix_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_size" ):
                listener.enterMatrix_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_size" ):
                listener.exitMatrix_size(self)




    def matrix_size(self):

        localctx = MY_LANGParser.Matrix_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_matrix_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MY_LANGParser.M_SIZE)
            self.state = 77
            self.match(MY_LANGParser.LEFT_P)
            self.state = 78
            self.match(MY_LANGParser.ID)
            self.state = 79
            self.match(MY_LANGParser.COMA)
            self.state = 80
            self.match(MY_LANGParser.ID)
            self.state = 81
            self.match(MY_LANGParser.COMA)
            self.state = 82
            self.match(MY_LANGParser.ID)
            self.state = 83
            self.match(MY_LANGParser.RIGHT_P)
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(MY_LANGParser.INT)
                pass

            elif la_ == 2:
                self.state = 87
                self.match(MY_LANGParser.REAL)
                pass

            elif la_ == 3:
                self.state = 88
                self.match(MY_LANGParser.ID)
                pass

            elif la_ == 4:
                self.state = 89
                self.match(MY_LANGParser.LEFT_P)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(MY_LANGParser.RIGHT_P)
                pass

            elif la_ == 5:
                self.state = 93
                self.matrix()
                pass

            elif la_ == 6:
                self.state = 94
                self.matrix_elem()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 98
                        self.match(MY_LANGParser.MUL)
                        self.state = 99
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 101
                        self.match(MY_LANGParser.DIV)
                        self.state = 102
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 104
                        self.match(MY_LANGParser.ADD)
                        self.state = 105
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 107
                        self.match(MY_LANGParser.SUB)
                        self.state = 108
                        self.expr(8)
                        pass

             
                self.state = 113
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
        self.enterRule(localctx, 20, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MY_LANGParser.T__0)
            self.state = 115
            self.match(MY_LANGParser.INT)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 116
                self.match(MY_LANGParser.COMA)
                self.state = 117
                self.match(MY_LANGParser.INT)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
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
        self.enterRule(localctx, 22, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MY_LANGParser.T__0)
            self.state = 126
            self.row()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 127
                self.match(MY_LANGParser.COMA)
                self.state = 128
                self.row()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
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
        self.enterRule(localctx, 24, self.RULE_scale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MY_LANGParser.SCALE)
            self.state = 137
            self.match(MY_LANGParser.LEFT_P)
            self.state = 138
            self.match(MY_LANGParser.ID)
            self.state = 139
            self.match(MY_LANGParser.COMA)
            self.state = 140
            self.match(MY_LANGParser.INT)
            self.state = 141
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
        self._predicates[9] = self.expr_sempred
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
         




