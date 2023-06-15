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


    # Enter a parse tree produced by MY_LANGParser#arg_list.
    def enterArg_list(self, ctx:MY_LANGParser.Arg_listContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#arg_list.
    def exitArg_list(self, ctx:MY_LANGParser.Arg_listContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#function_header.
    def enterFunction_header(self, ctx:MY_LANGParser.Function_headerContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#function_header.
    def exitFunction_header(self, ctx:MY_LANGParser.Function_headerContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#define.
    def enterDefine(self, ctx:MY_LANGParser.DefineContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#define.
    def exitDefine(self, ctx:MY_LANGParser.DefineContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#end_function.
    def enterEnd_function(self, ctx:MY_LANGParser.End_functionContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#end_function.
    def exitEnd_function(self, ctx:MY_LANGParser.End_functionContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#call_function.
    def enterCall_function(self, ctx:MY_LANGParser.Call_functionContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#call_function.
    def exitCall_function(self, ctx:MY_LANGParser.Call_functionContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#loop.
    def enterLoop(self, ctx:MY_LANGParser.LoopContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#loop.
    def exitLoop(self, ctx:MY_LANGParser.LoopContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#loop_header.
    def enterLoop_header(self, ctx:MY_LANGParser.Loop_headerContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#loop_header.
    def exitLoop_header(self, ctx:MY_LANGParser.Loop_headerContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#loop_end.
    def enterLoop_end(self, ctx:MY_LANGParser.Loop_endContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#loop_end.
    def exitLoop_end(self, ctx:MY_LANGParser.Loop_endContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#struct.
    def enterStruct(self, ctx:MY_LANGParser.StructContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#struct.
    def exitStruct(self, ctx:MY_LANGParser.StructContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#create_structure.
    def enterCreate_structure(self, ctx:MY_LANGParser.Create_structureContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#create_structure.
    def exitCreate_structure(self, ctx:MY_LANGParser.Create_structureContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#part_structure.
    def enterPart_structure(self, ctx:MY_LANGParser.Part_structureContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#part_structure.
    def exitPart_structure(self, ctx:MY_LANGParser.Part_structureContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#conditional_stat.
    def enterConditional_stat(self, ctx:MY_LANGParser.Conditional_statContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#conditional_stat.
    def exitConditional_stat(self, ctx:MY_LANGParser.Conditional_statContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#conditional_header.
    def enterConditional_header(self, ctx:MY_LANGParser.Conditional_headerContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#conditional_header.
    def exitConditional_header(self, ctx:MY_LANGParser.Conditional_headerContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#else_part.
    def enterElse_part(self, ctx:MY_LANGParser.Else_partContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#else_part.
    def exitElse_part(self, ctx:MY_LANGParser.Else_partContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#bool_stat.
    def enterBool_stat(self, ctx:MY_LANGParser.Bool_statContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#bool_stat.
    def exitBool_stat(self, ctx:MY_LANGParser.Bool_statContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#typ.
    def enterTyp(self, ctx:MY_LANGParser.TypContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#typ.
    def exitTyp(self, ctx:MY_LANGParser.TypContext):
        pass


    # Enter a parse tree produced by MY_LANGParser#expr.
    def enterExpr(self, ctx:MY_LANGParser.ExprContext):
        pass

    # Exit a parse tree produced by MY_LANGParser#expr.
    def exitExpr(self, ctx:MY_LANGParser.ExprContext):
        pass



del MY_LANGParser