from MY_LANGListener import MY_LANGListener
from LLVMGenerator import LLVMGenerator
from MY_LANGParser import MY_LANGParser


class Value:
    def __init__(self, name_of_variable, type_of_variable, size=None):
        self.name = name_of_variable
        self.typ = type_of_variable
        self.size = size
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

    def print_variables(self):
        for ele in self.variables:
            print(ele)
            print(self.variables[ele])

    def exitProg(self, ctx):
        self.gen.print_main_text()
        # self.print_stack()
        # self.print_variables()
        pass

    def exitAssign(self, ctx):
        self.n+=1
        v = self.stack.pop()
        if ctx.ID():
            var_name = ctx.ID().getText()
            if v.typ=="INT":
                if var_name in self.variables.keys():
                    print("doned already")
                    name = self.variables[var_name].name    
                    self.gen.asign_i32(name,v.name)
                else: 
                    self.variables[var_name]=Value(f"%{self.n}","INT")
                    self.gen.alloca(f"%{self.n}","i32")
                    self.gen.asign_i32(f"%{self.n}",v.name)
            if v.typ=="MATRIX":
                self.variables[var_name]=Value(v.name,"Matrix",v.size)
        elif ctx.matrix_elem():
            if v.typ != "INT":
                raise RuntimeError("Only Int are supported for matrix")
            ctx=ctx.matrix_elem()
            self.gen.alloca(f"%{self.n}","i32")
            self.gen.asign_i32(f"%{self.n}",v.name)
            name = ctx.ID().getText()
            value = self.variables[name]
            index = int(value.name[1:])
            y = int(ctx.INT()[0].getText())
            x = int(ctx.INT()[1].getText())
            our_data_id = index+1+y*value.size[0]+x
            self.gen.asign_i32(f'%{our_data_id}',f"%{self.n}")
            
    def exitScale(self, ctx):
        variable_local_name = ctx.ID().getText()
        value_to_scale = ctx.INT().getText()
        

        Matrix = self.variables[variable_local_name]
        if Matrix.typ != "Matrix":
            raise TypeError("Scale is only supported for Matrixes")
        x,y = Matrix.size
        Starting_index = int(Matrix.name[1:])+1
        for i in range(x*y):
            id = f'{Starting_index+i}'
            self.gen.mul_i32(id, f"%{id}", value_to_scale)
            
        

    def exitPrint(self, ctx):
        self.n+=1
        v = self.stack.pop()
        if v.typ == "INT":
            self.gen.print_i32(v.name,self.n)
        self.n+=1

    def exitRead(self, ctx):
        self.n+=1
        pass
        # Perform read logic here using id

    def exitExpr(self, ctx):
        #TODO ZAIMPLEMENTOWAĆ DZIELENIE. WEWNĄTRZ KAŻDEFO IFA ZROBIĆ OPERACJE DLA DWÓCH INTÓW I REALÓW ODDZIELNIE (v1.typ, v2.typ daje typy zmiennych) 
        #  w LLVM będą różnice (nie i32). DO ZASTANOWIENIA CZY ZGŁASZAMY BŁĄD JAK SĄ MIESZANE TYPY (MOIM ZDANIEM WTEDY INT RZUTUJEMY NA FLOAT) 
        #
        self.n+=1
        if ctx.matrix():
            ctx = ctx.matrix()
            number_of_rows = len(ctx.row())
            row_size = len(ctx.row()[0].INT())
            identifier_for_matrix = self.n
            y=0
            for row_ctx in ctx.row():
                if len(row_ctx.INT()) !=row_size:
                    raise NotImplementedError("Only rectangled matrixes designed")
                for i in row_ctx.INT():
                    self.n+=1
                    self.gen.alloca(f"%{self.n}","i32")
                    self.gen.asign_i32(f"%{self.n}",i.getText())
            self.stack.append(Value(f"%{identifier_for_matrix}", "MATRIX",size=(number_of_rows,row_size)))    
        
        elif ctx.INT():
            self.stack.append(Value(ctx.INT().getText(),"INT"))

        elif ctx.REAL():
            self.stack.append(Value(ctx.REAL().getText()+"0","REAL"))

        elif ctx.ID():
            self.stack.append(self.variables[ctx.ID().getText()])

        elif ctx.ADD():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.add_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))

        elif ctx.SUB():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.sub_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))

        elif ctx.DIV():
            raise NotImplementedError("not implemented YET")

        elif ctx.MUL():
            v1=self.stack.pop()
            v2=self.stack.pop()
            self.gen.mul_i32(self.n, v1.name, v2.name)
            self.stack.append(Value(f"%{self.n}","INT"))

        
    
        