# Generated from MY_LANG.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,18,115,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,4,5,56,8,
        5,11,5,12,5,57,1,6,4,6,61,8,6,11,6,12,6,62,1,6,1,6,5,6,67,8,6,10,
        6,12,6,70,9,6,1,7,4,7,73,8,7,11,7,12,7,74,1,7,1,7,5,7,79,8,7,10,
        7,12,7,82,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,
        12,1,13,1,13,1,14,1,14,5,14,100,8,14,10,14,12,14,103,9,14,1,15,1,
        15,1,16,1,16,1,17,4,17,110,8,17,11,17,12,17,111,1,17,1,17,0,0,18,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,1,0,4,1,0,48,57,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,121,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,
        0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,
        0,0,33,1,0,0,0,0,35,1,0,0,0,1,37,1,0,0,0,3,39,1,0,0,0,5,41,1,0,0,
        0,7,43,1,0,0,0,9,49,1,0,0,0,11,55,1,0,0,0,13,60,1,0,0,0,15,72,1,
        0,0,0,17,85,1,0,0,0,19,87,1,0,0,0,21,89,1,0,0,0,23,91,1,0,0,0,25,
        93,1,0,0,0,27,95,1,0,0,0,29,97,1,0,0,0,31,104,1,0,0,0,33,106,1,0,
        0,0,35,109,1,0,0,0,37,38,5,91,0,0,38,2,1,0,0,0,39,40,5,44,0,0,40,
        4,1,0,0,0,41,42,5,93,0,0,42,6,1,0,0,0,43,44,5,80,0,0,44,45,5,82,
        0,0,45,46,5,73,0,0,46,47,5,78,0,0,47,48,5,84,0,0,48,8,1,0,0,0,49,
        50,5,82,0,0,50,51,5,69,0,0,51,52,5,65,0,0,52,53,5,68,0,0,53,10,1,
        0,0,0,54,56,7,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,12,1,0,0,0,59,61,7,0,0,0,60,59,1,0,0,0,61,62,1,0,0,
        0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,68,5,46,0,0,65,67,
        7,0,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,
        69,14,1,0,0,0,70,68,1,0,0,0,71,73,7,0,0,0,72,71,1,0,0,0,73,74,1,
        0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,80,5,46,0,0,77,
        79,7,0,0,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,
        0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,70,0,0,84,16,1,0,0,0,85,86,
        5,42,0,0,86,18,1,0,0,0,87,88,5,47,0,0,88,20,1,0,0,0,89,90,5,43,0,
        0,90,22,1,0,0,0,91,92,5,45,0,0,92,24,1,0,0,0,93,94,5,61,0,0,94,26,
        1,0,0,0,95,96,5,59,0,0,96,28,1,0,0,0,97,101,7,1,0,0,98,100,7,2,0,
        0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,
        30,1,0,0,0,103,101,1,0,0,0,104,105,5,40,0,0,105,32,1,0,0,0,106,107,
        5,41,0,0,107,34,1,0,0,0,108,110,7,3,0,0,109,108,1,0,0,0,110,111,
        1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,
        6,17,0,0,114,36,1,0,0,0,8,0,57,62,68,74,80,101,111,1,6,0,0
    ]

class MY_LANGLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    PRINT = 4
    READ = 5
    INT = 6
    DOUBLE = 7
    FLOAT = 8
    MUL = 9
    DIV = 10
    ADD = 11
    SUB = 12
    SET = 13
    EOE = 14
    ID = 15
    LEFT_P = 16
    RIGHT_P = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "','", "']'", "'PRINT'", "'READ'", "'*'", "'/'", "'+'", 
            "'-'", "'='", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "READ", "INT", "DOUBLE", "FLOAT", "MUL", "DIV", "ADD", 
            "SUB", "SET", "EOE", "ID", "LEFT_P", "RIGHT_P", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "PRINT", "READ", "INT", "DOUBLE", 
                  "FLOAT", "MUL", "DIV", "ADD", "SUB", "SET", "EOE", "ID", 
                  "LEFT_P", "RIGHT_P", "WS" ]

    grammarFileName = "MY_LANG.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


