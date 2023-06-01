# Generated from MY_LANG.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MY_LANGParser import MY_LANGParser
else:
    from MY_LANGParser import MY_LANGParser

# This class defines a complete listener for a parse tree produced by MY_LANGParser.
class MY_LANGListener(ParseTreeListener):

    # Enter a parse tree produced by MY_LANGParser#prog.
    def enterProg(self, ctx:MY_LANGParser.ProgContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#prog.
    def exitProg(self, ctx:MY_LANGParser.ProgContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#statements.
    def enterStatements(self, ctx:MY_LANGParser.StatementsContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#statements.
    def exitStatements(self, ctx:MY_LANGParser.StatementsContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#statement.
    def enterStatement(self, ctx:MY_LANGParser.StatementContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#statement.
    def exitStatement(self, ctx:MY_LANGParser.StatementContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#assign.
    def enterAssign(self, ctx:MY_LANGParser.AssignContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#assign.
    def exitAssign(self, ctx:MY_LANGParser.AssignContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#print.
    def enterPrint(self, ctx:MY_LANGParser.PrintContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#print.
    def exitPrint(self, ctx:MY_LANGParser.PrintContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#read.
    def enterRead(self, ctx:MY_LANGParser.ReadContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#read.
    def exitRead(self, ctx:MY_LANGParser.ReadContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#matrix_elem.
    def enterMatrix_elem(self, ctx:MY_LANGParser.Matrix_elemContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#matrix_elem.
    def exitMatrix_elem(self, ctx:MY_LANGParser.Matrix_elemContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#expr.
    def enterExpr(self, ctx:MY_LANGParser.ExprContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#expr.
    def exitExpr(self, ctx:MY_LANGParser.ExprContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#row.
    def enterRow(self, ctx:MY_LANGParser.RowContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#row.
    def exitRow(self, ctx:MY_LANGParser.RowContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#matrix.
    def enterMatrix(self, ctx:MY_LANGParser.MatrixContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#matrix.
    def exitMatrix(self, ctx:MY_LANGParser.MatrixContext):
        pass



del MY_LANGParser