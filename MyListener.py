from MutterspracheListener import MutterspracheListener
from MutterspracheParser import MutterspracheParser

# class Mylistener(MutterspracheListener):
#     def exitAssign(self, ctx: MutterspracheParser.AssignContext):
#         variable_name = ctx.ID().getText()
#         expr_value = ctx.expr().getText()
#         llvm_code = f"%{variable_name} = alloca i32\nstore i32 {expr_value}, i32* %{variable_name}"
#         print("LLVM IR code for assignment:\n", llvm_code)       

class MyListener(MutterspracheListener):
    def enterProg(self, ctx):
        pass

    def exitProg(self, ctx):
        pass

    def enterStatements(self, ctx):
        pass

    def exitStatements(self, ctx):
        pass

    def enterStatement(self, ctx):
        pass

    def exitStatement(self, ctx):
        pass

    def enterAssign(self, ctx):
        pass

    def exitAssign(self, ctx):
        id = ctx.ID().getText()
        expr_value = self.visit(ctx.expr())
        # Perform assignment logic here using id and expr_value

    def enterPrint(self, ctx):
        pass

    def exitPrint(self, ctx):
        expr_value = self.visit(ctx.expr())
        # Perform print logic here using expr_value

    def enterRead(self, ctx):
        pass

    def exitRead(self, ctx):
        id = ctx.ID().getText()
        # Perform read logic here using id

    def enterExpr(self, ctx):
        pass

    def exitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.REAL():
            return float(ctx.REAL().getText())
        elif ctx.ID():
            return ctx.ID().getText()
        elif len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            # Perform arithmetic operation logic here using left, right, and op
        elif ctx.expr(0):
            return self.visit(ctx.expr(0))
        