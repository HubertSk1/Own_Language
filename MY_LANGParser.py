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
        4,1,20,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,1,
        1,5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,86,8,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,
        11,100,8,11,10,11,12,11,103,9,11,1,11,0,1,22,12,0,2,4,6,8,10,12,
        14,16,18,20,22,0,1,1,0,1,2,103,0,24,1,0,0,0,2,31,1,0,0,0,4,37,1,
        0,0,0,6,41,1,0,0,0,8,45,1,0,0,0,10,50,1,0,0,0,12,55,1,0,0,0,14,61,
        1,0,0,0,16,67,1,0,0,0,18,72,1,0,0,0,20,75,1,0,0,0,22,85,1,0,0,0,
        24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,0,0,27,30,3,4,2,0,28,30,3,16,
        8,0,29,27,1,0,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,38,3,8,4,0,35,38,3,6,3,0,36,
        38,3,10,5,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,39,1,0,
        0,0,39,40,5,15,0,0,40,5,1,0,0,0,41,42,5,17,0,0,42,43,5,14,0,0,43,
        44,3,22,11,0,44,7,1,0,0,0,45,46,5,6,0,0,46,47,5,18,0,0,47,48,3,22,
        11,0,48,49,5,19,0,0,49,9,1,0,0,0,50,51,5,7,0,0,51,52,5,18,0,0,52,
        53,5,17,0,0,53,54,5,19,0,0,54,11,1,0,0,0,55,56,3,20,10,0,56,57,5,
        17,0,0,57,58,5,16,0,0,58,59,3,20,10,0,59,60,5,17,0,0,60,13,1,0,0,
        0,61,62,5,3,0,0,62,63,5,17,0,0,63,64,5,18,0,0,64,65,3,12,6,0,65,
        66,5,19,0,0,66,15,1,0,0,0,67,68,3,14,7,0,68,69,5,4,0,0,69,70,3,4,
        2,0,70,71,3,18,9,0,71,17,1,0,0,0,72,73,5,5,0,0,73,74,5,17,0,0,74,
        19,1,0,0,0,75,76,7,0,0,0,76,21,1,0,0,0,77,78,6,11,-1,0,78,86,5,8,
        0,0,79,86,5,9,0,0,80,86,5,17,0,0,81,82,5,18,0,0,82,83,3,22,11,0,
        83,84,5,19,0,0,84,86,1,0,0,0,85,77,1,0,0,0,85,79,1,0,0,0,85,80,1,
        0,0,0,85,81,1,0,0,0,86,101,1,0,0,0,87,88,10,8,0,0,88,89,5,10,0,0,
        89,100,3,22,11,9,90,91,10,7,0,0,91,92,5,11,0,0,92,100,3,22,11,8,
        93,94,10,6,0,0,94,95,5,12,0,0,95,100,3,22,11,7,96,97,10,5,0,0,97,
        98,5,13,0,0,98,100,3,22,11,6,99,87,1,0,0,0,99,90,1,0,0,0,99,93,1,
        0,0,0,99,96,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,
        0,102,23,1,0,0,0,103,101,1,0,0,0,6,29,31,37,85,99,101
    ]

class MY_LANGParser ( Parser ):

    grammarFileName = "MY_LANG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'INT'", "'REAL'", "'DEFINE'", "'BEGIN'", 
                     "'RETURN'", "'PRINT'", "'READ'", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "'='", "';'", "','", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT_TYPE", "REAL_TYPE", "DEF", "BEGIN", 
                      "RETURN", "PRINT", "READ", "INT", "REAL", "MUL", "DIV", 
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
    RULE_end_function = 9
    RULE_typ = 10
    RULE_expr = 11

    ruleNames =  [ "prog", "statements", "statement", "assign", "print", 
                   "read", "arg_list", "function_header", "define", "end_function", 
                   "typ", "expr" ]

    EOF = Token.EOF
    INT_TYPE=1
    REAL_TYPE=2
    DEF=3
    BEGIN=4
    RETURN=5
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
            self.state = 24
            self.statements()
            self.state = 25
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


        def define(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.DefineContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.DefineContext,i)


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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131272) != 0):
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 7, 17]:
                    self.state = 27
                    self.statement()
                    pass
                elif token in [3]:
                    self.state = 28
                    self.define()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 33
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
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 34
                self.print_()
                pass
            elif token in [17]:
                self.state = 35
                self.assign()
                pass
            elif token in [7]:
                self.state = 36
                self.read()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 39
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
            self.state = 41
            self.match(MY_LANGParser.ID)
            self.state = 42
            self.match(MY_LANGParser.SET)
            self.state = 43
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
            self.state = 45
            self.match(MY_LANGParser.PRINT)
            self.state = 46
            self.match(MY_LANGParser.LEFT_P)
            self.state = 47
            self.expr(0)
            self.state = 48
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
            self.state = 50
            self.match(MY_LANGParser.READ)
            self.state = 51
            self.match(MY_LANGParser.LEFT_P)
            self.state = 52
            self.match(MY_LANGParser.ID)
            self.state = 53
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

        def typ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MY_LANGParser.TypContext)
            else:
                return self.getTypedRuleContext(MY_LANGParser.TypContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MY_LANGParser.ID)
            else:
                return self.getToken(MY_LANGParser.ID, i)

        def COMA(self):
            return self.getToken(MY_LANGParser.COMA, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.typ()
            self.state = 56
            self.match(MY_LANGParser.ID)

            self.state = 57
            self.match(MY_LANGParser.COMA)
            self.state = 58
            self.typ()
            self.state = 59
            self.match(MY_LANGParser.ID)
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
            self.state = 61
            self.match(MY_LANGParser.DEF)
            self.state = 62
            self.match(MY_LANGParser.ID)
            self.state = 63
            self.match(MY_LANGParser.LEFT_P)
            self.state = 64
            self.arg_list()
            self.state = 65
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

        def statement(self):
            return self.getTypedRuleContext(MY_LANGParser.StatementContext,0)


        def end_function(self):
            return self.getTypedRuleContext(MY_LANGParser.End_functionContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.function_header()
            self.state = 68
            self.match(MY_LANGParser.BEGIN)
            self.state = 69
            self.statement()
            self.state = 70
            self.end_function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MY_LANGParser.RETURN, 0)

        def ID(self):
            return self.getToken(MY_LANGParser.ID, 0)

        def getRuleIndex(self):
            return MY_LANGParser.RULE_end_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_function" ):
                listener.enterEnd_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_function" ):
                listener.exitEnd_function(self)




    def end_function(self):

        localctx = MY_LANGParser.End_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_end_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MY_LANGParser.RETURN)
            self.state = 73
            self.match(MY_LANGParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.state = 75
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 78
                self.match(MY_LANGParser.INT)
                pass
            elif token in [9]:
                self.state = 79
                self.match(MY_LANGParser.REAL)
                pass
            elif token in [17]:
                self.state = 80
                self.match(MY_LANGParser.ID)
                pass
            elif token in [18]:
                self.state = 81
                self.match(MY_LANGParser.LEFT_P)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(MY_LANGParser.RIGHT_P)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 88
                        self.match(MY_LANGParser.MUL)
                        self.state = 89
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 91
                        self.match(MY_LANGParser.DIV)
                        self.state = 92
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 94
                        self.match(MY_LANGParser.ADD)
                        self.state = 95
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MY_LANGParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 97
                        self.match(MY_LANGParser.SUB)
                        self.state = 98
                        self.expr(6)
                        pass

             
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
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
         




