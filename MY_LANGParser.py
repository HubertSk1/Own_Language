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
        4,1,20,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,5,1,27,8,1,10,
        1,12,1,30,9,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,2,1,2,1,2,3,2,41,
        8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,5,6,62,8,6,10,6,12,6,65,9,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,5,8,77,8,8,10,8,12,8,80,9,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,92,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,5,9,106,8,9,10,9,12,9,109,9,9,1,10,1,10,1,10,0,
        1,18,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,1,2,114,0,22,1,0,0,0,
        2,28,1,0,0,0,4,40,1,0,0,0,6,44,1,0,0,0,8,48,1,0,0,0,10,53,1,0,0,
        0,12,58,1,0,0,0,14,66,1,0,0,0,16,73,1,0,0,0,18,91,1,0,0,0,20,110,
        1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,27,3,16,8,0,
        26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,34,1,
        0,0,0,30,28,1,0,0,0,31,33,3,4,2,0,32,31,1,0,0,0,33,36,1,0,0,0,34,
        32,1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,34,1,0,0,0,37,41,3,8,4,
        0,38,41,3,6,3,0,39,41,3,10,5,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,
        1,0,0,0,41,42,1,0,0,0,42,43,5,15,0,0,43,5,1,0,0,0,44,45,5,17,0,0,
        45,46,5,14,0,0,46,47,3,18,9,0,47,7,1,0,0,0,48,49,5,6,0,0,49,50,5,
        18,0,0,50,51,3,18,9,0,51,52,5,19,0,0,52,9,1,0,0,0,53,54,5,7,0,0,
        54,55,5,18,0,0,55,56,5,17,0,0,56,57,5,19,0,0,57,11,1,0,0,0,58,63,
        5,17,0,0,59,60,5,16,0,0,60,62,5,17,0,0,61,59,1,0,0,0,62,65,1,0,0,
        0,63,61,1,0,0,0,63,64,1,0,0,0,64,13,1,0,0,0,65,63,1,0,0,0,66,67,
        5,3,0,0,67,68,3,20,10,0,68,69,5,17,0,0,69,70,5,18,0,0,70,71,3,12,
        6,0,71,72,5,19,0,0,72,15,1,0,0,0,73,74,3,14,7,0,74,78,5,4,0,0,75,
        77,3,4,2,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,
        0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,5,0,0,82,17,1,0,0,0,83,84,
        6,9,-1,0,84,92,5,8,0,0,85,92,5,9,0,0,86,92,5,17,0,0,87,88,5,18,0,
        0,88,89,3,18,9,0,89,90,5,19,0,0,90,92,1,0,0,0,91,83,1,0,0,0,91,85,
        1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,92,107,1,0,0,0,93,94,10,8,0,
        0,94,95,5,10,0,0,95,106,3,18,9,9,96,97,10,7,0,0,97,98,5,11,0,0,98,
        106,3,18,9,8,99,100,10,6,0,0,100,101,5,12,0,0,101,106,3,18,9,7,102,
        103,10,5,0,0,103,104,5,13,0,0,104,106,3,18,9,6,105,93,1,0,0,0,105,
        96,1,0,0,0,105,99,1,0,0,0,105,102,1,0,0,0,106,109,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,19,1,0,0,0,109,107,1,0,0,0,110,111,7,
        0,0,0,111,21,1,0,0,0,8,28,34,40,63,78,91,105,107
    ]

class MY_LANGParser ( Parser ):

    grammarFileName = "MY_LANG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'real'", "'DEFINE'", "'BEGIN'", 
                     "'END'", "'PRINT'", "'READ'", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'='", "';'", "','", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT_TYPE", "REAL_TYPE", "DEF", "BEGIN", 
                      "END", "PRINT", "READ", "INT", "REAL", "MUL", "DIV", 
                      "ADD", "SUB", "SET", "EOE", "COMA", "ID", "LEFT_P", 
                      "RIGHT_P", "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_assign = 3
    RULE_print = 4
    RULE_read = 5
    RULE_arg_list = 6
    RULE_function_header = 7
    RULE_define = 8
    RULE_expr = 9
    RULE_typ = 10

    ruleNames =  [ "prog", "statements", "statement", "assign", "print", 
                   "read", "arg_list", "function_header", "define", "expr", 
                   "typ" ]

    EOF = Token.EOF
    INT_TYPE=1
    REAL_TYPE=2
    DEF=3
    BEGIN=4
    END=5
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

        def define(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.DefineContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.DefineContext,i)


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
            while _la==3:
                self.state = 25
                self.define()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131264) != 0):
                self.state = 31
                self.statement()
                self.state = 36
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 37
                self.print_()
                pass
            elif token in [17]:
                self.state = 38
                self.assign()
                pass
            elif token in [7]:
                self.state = 39
                self.read()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 42
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

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def SET(self):
            return self.getToken(MY_LANGParser.SET, 0)

        def expr(self):
            return self.getTypedRuleContext(MY_LANGParser.ExprContext,0)


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
            self.state = 44
            self.match(MY_LANGParser.ID)
            self.state = 45
            self.match(MY_LANGParser.SET)
            self.state = 46
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
            self.state = 48
            self.match(MY_LANGParser.PRINT)
            self.state = 49
            self.match(MY_LANGParser.LEFT_P)
            self.state = 50
            self.expr(0)
            self.state = 51
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
            self.state = 53
            self.match(MY_LANGParser.READ)
            self.state = 54
            self.match(MY_LANGParser.LEFT_P)
            self.state = 55
            self.match(MY_LANGParser.ID)
            self.state = 56
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return MY_LANGParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = MY_LANGParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MY_LANGParser.ID)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 59
                self.match(MY_LANGParser.COMA)
                self.state = 60
                self.match(MY_LANGParser.ID)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(MY_LANGParser.DEF, 0)

        def typ(self):
            return self.getTypedRuleContext(MY_LANGParser.TypContext,0)


        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def LEFT_P(self):
            return self.getToken(MY_LANGParser.LEFT_P, 0)

        def arg_list(self):
            return self.getTypedRuleContext(MY_LANGParser.Arg_listContext,0)


        def RIGHT_P(self):
            return self.getToken(MY_LANGParser.RIGHT_P, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_function_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_header" ):
                listener.enterFunction_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_header" ):
                listener.exitFunction_header(self)




    def function_header(self):

        localctx = MY_LANGParser.Function_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MY_LANGParser.DEF)
            self.state = 67
            self.typ()
            self.state = 68
            self.match(MY_LANGParser.ID)
            self.state = 69
            self.match(MY_LANGParser.LEFT_P)
            self.state = 70
            self.arg_list()
            self.state = 71
            self.match(MY_LANGParser.RIGHT_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_header(self):
            return self.getTypedRuleContext(MY_LANGParser.Function_headerContext,0)


        def BEGIN(self):
            return self.getToken(MY_LANGParser.BEGIN, 0)

        def END(self):
            return self.getToken(MY_LANGParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.StatementContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.StatementContext,i)


        def getRuleIndex(self):
            return MY_LANGParser.RULE_define

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine" ):
                listener.enterDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine" ):
                listener.exitDefine(self)




    def define(self):

        localctx = MY_LANGParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_define)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.function_header()
            self.state = 74
            self.match(MY_LANGParser.BEGIN)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131264) != 0):
                self.state = 75
                self.statement()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(MY_LANGParser.END)
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
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 84
                self.match(MY_LANGParser.INT)
                pass
            elif token in [9]:
                self.state = 85
                self.match(MY_LANGParser.REAL)
                pass
            elif token in [17]:
                self.state = 86
                self.match(MY_LANGParser.ID)
                pass
            elif token in [18]:
                self.state = 87
                self.match(MY_LANGParser.LEFT_P)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(MY_LANGParser.RIGHT_P)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 94
                        self.match(MY_LANGParser.MUL)
                        self.state = 95
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 97
                        self.match(MY_LANGParser.DIV)
                        self.state = 98
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 100
                        self.match(MY_LANGParser.ADD)
                        self.state = 101
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 103
                        self.match(MY_LANGParser.SUB)
                        self.state = 104
                        self.expr(6)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MY_LANGParser.INT_TYPE, 0)

        def REAL_TYPE(self):
            return self.getToken(MY_LANGParser.REAL_TYPE, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = MY_LANGParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




