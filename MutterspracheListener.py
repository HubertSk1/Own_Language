# Generated from Muttersprache.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MutterspracheParser import MutterspracheParser
else:
    from MutterspracheParser import MutterspracheParser

# This class defines a complete listener for a parse tree produced by MutterspracheParser.
class MutterspracheListener(ParseTreeListener):

    # Enter a parse tree produced by MutterspracheParser#prog.
    def enterProg(self, ctx:MutterspracheParser.ProgContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#prog.
    def exitProg(self, ctx:MutterspracheParser.ProgContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#statements.
    def enterStatements(self, ctx:MutterspracheParser.StatementsContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#statements.
    def exitStatements(self, ctx:MutterspracheParser.StatementsContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#statement.
    def enterStatement(self, ctx:MutterspracheParser.StatementContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#statement.
    def exitStatement(self, ctx:MutterspracheParser.StatementContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#assign.
    def enterAssign(self, ctx:MutterspracheParser.AssignContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#assign.
    def exitAssign(self, ctx:MutterspracheParser.AssignContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#print.
    def enterPrint(self, ctx:MutterspracheParser.PrintContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#print.
    def exitPrint(self, ctx:MutterspracheParser.PrintContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#read.
    def enterRead(self, ctx:MutterspracheParser.ReadContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#read.
    def exitRead(self, ctx:MutterspracheParser.ReadContext):
        pass


    # Enter a parse tree produced by MutterspracheParser#expr.
    def enterExpr(self, ctx:MutterspracheParser.ExprContext):
        pass

    # Exit a parse tree produced by MutterspracheParser#expr.
    def exitExpr(self, ctx:MutterspracheParser.ExprContext):
        pass



del MutterspracheParser