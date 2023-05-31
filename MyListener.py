from MY_LANGListener import MY_LANGListener
from LLVMGenerator import LLVMGenerator


class Value:
    def __init__(self, name_of_variable, type_of_variable):
        self.name = name_of_variable
        self.typ = type_of_variable
    def __str__(self):
        return f"Variable {self.name} of type {self.typ}"

class MyListener(MY_LANGListener):
    def __init__(self):
        self.stack = []
        self.variables = dict() # {"Local_Name": Value}
        self.n = 1
        self.gen = LLVMGenerator()

    def print_stack(self):
        for ele in self.stack:
            print(ele)

    # def print_variables(self):
    #     for ele in self.variables:
    #         print(ele)
    #         print(self.variables[ele])

    def enterProg(self, ctx):
        self.n+=1
        pass

    def exitProg(self, ctx):
        self.gen.print_main_text()
        self.print_stack()
        # self.print_variables()
        pass

    def enterStatements(self, ctx):
        pass

    def exitStatements(self, ctx):
        self.n+=1
        pass

    def enterStatement(self, ctx):
        
        pass

    def exitStatement(self, ctx):
        self.n+=1
        pass

    def enterAssign(self, ctx):
        pass

    def exitAssign(self, ctx):
        self.n+=1
        v = self.stack.pop()
        var_name = ctx.ID().getText()
        if v.typ=="INT":
            self.variables[var_name]=Value(f"%{self.n}","INT")
            self.gen.alloca(f"%{self.n}","i32")
            self.gen.asign_i32(f"%{self.n}",v.name)
        pass

    def enterPrint(self, ctx):
        pass

    def exitPrint(self, ctx):
        self.n+=1
        v = self.stack.pop()
        if v.typ == "INT":
            self.gen.print_i32(v.name,self.n)
        self.n+=1
    def enterRead(self, ctx):
        pass

    def exitRead(self, ctx):
        self.n+=1
        pass
        # Perform read logic here using id

    def enterExpr(self, ctx):
        pass

    def exitExpr(self, ctx):
        #TODO ZAIMPLEMENTOWAĆ DZIELENIE. WEWNĄTRZ KAŻDEFO IFA ZROBIĆ OPERACJE DLA DWÓCH INTÓW I REALÓW ODDZIELNIE (v1.typ, v2.typ daje typy zmiennych) 
        #  w LLVM będą różnice (nie i32). DO ZASTANOWIENIA CZY ZGŁASZAMY BŁĄD JAK SĄ MIESZANE TYPY (MOIM ZDANIEM WTEDY INT RZUTUJEMY NA FLOAT) 
        #
        self.n+=1
        if ctx.INT():
            self.stack.append(Value(ctx.INT().getText(),"INT"))
        if ctx.REAL():
            self.stack.append(Value(ctx.REAL().getText()+"0","REAL"))
        if ctx.ID():
            self.stack.append(self.variables[ctx.ID().getText()])

        if ctx.ADD():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.add_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))
        if ctx.SUB():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.sub_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))
        if ctx.DIV():
            raise NotImplementedError("not implemented YET")

        if ctx.MUL():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.mul_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))
        