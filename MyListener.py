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
            elif v.typ == "REAL":
                if var_name in self.variables.keys():
                    name = self.variables[var_name].name    
                    self.gen.asign_float(name,v.name)
                else:
                    self.variables[var_name] = Value(f"%{self.n}", "REAL")
                    self.gen.alloca(f"%{self.n}", "float")
                    self.gen.asign_float(f"%{self.n}", v.name)
            elif v.typ=="MATRIX":
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

    def exitMatrix_add(self, ctx):
        name2 = ctx.ID()[0].getText()
        name1 = ctx.ID()[1].getText()
        value1 = self.variables[name1]
        value2 = self.variables[name2]
        if value1.size  != value2.size:
            raise ValueError(f"matrixes {name1} and {name2} need to be the same sizes")
        index1 = int(value1.name[1:])+1
        index2 = int(value2.name[1:])+1
        for s in range (value1.size[1]*value1.size[0]):
            self.gen.add_i32(f"{index1+s}",f"%{index2+s}",f"%{index1+s}")

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
        elif v.typ == "REAL":
            self.gen.printf_float(v.name,self.n)
        self.n+=1

    def exitRead(self, ctx):
        self.n+=1
        var_name = ctx.ID().getText()
        id=self.variables[var_name].name
        if self.variables[var_name].typ == "INT":
            self.gen.scanf_i32(id)
        elif self.variables[var_name].typ == "REAL":
            self.gen.scanf_float(id)
        self.n+=1

    def exitExpr(self, ctx):
        self.n+=1
        if ctx.matrix():
            ctx = ctx.matrix()
            number_of_rows = len(ctx.row())
            row_size = len(ctx.row()[0].INT())
            identifier_for_matrix = self.n
            y=0
            for row_ctx in ctx.row():
                x=0
                if len(row_ctx.INT()) !=row_size:
                    raise NotImplementedError("Only rectangled matrixes designed")
                for i in row_ctx.INT():
                    self.n+=1
                    self.gen.alloca(f"%{self.n}","i32")
                    self.gen.asign_i32(f"%{self.n}",i.getText())
            self.stack.append(Value(f"%{identifier_for_matrix}", "MATRIX",(number_of_rows,row_size)))    
        
        elif ctx.INT():
            self.stack.append(Value(ctx.INT().getText(),"INT"))

        elif ctx.REAL():
            self.stack.append(Value(ctx.REAL().getText()+"0","REAL"))

        elif ctx.ID():
            self.stack.append(self.variables[ctx.ID().getText()])

        elif ctx.matrix_elem():
            ctx = ctx.matrix_elem()
            name = ctx.ID().getText()
            value = self.variables[name]
            index = int(value.name[1:])
            y = int(ctx.INT()[0].getText())
            x = int(ctx.INT()[1].getText())
            our_data_id = index+1+y*value.size[0]+x
            self.stack.append(Value(f"%{our_data_id}", "INT"))

        elif ctx.ADD():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.add_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.add_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.n+=1
                self.gen.int_to_float(self.n, v1.name)
                self.gen.add_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.n+=1
                self.gen.int_to_float(self.n, v2.name)
                self.gen.add_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            else:
                raise TypeError(f"Unsupported type for add: {v1.typ}, {v2.typ}")
            

        elif ctx.SUB():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.sub_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
            
            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.sub_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.n+=1
                self.gen.int_to_float(self.n, v1.name)
                self.gen.sub_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.n+=1
                self.gen.int_to_float(self.n, v2.name)
                self.gen.sub_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            else:
                raise TypeError(f"Unsupported type for sub: {v1.typ}, {v2.typ}")

        elif ctx.DIV():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.div_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
                
            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.div_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.n+=1
                self.gen.int_to_float(self.n, v1.name)
                self.gen.div_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.n+=1
                self.gen.int_to_float(self.n, v2.name)
                self.gen.div_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            else:
                raise TypeError(f"Unsupported type for div: {v1.typ}, {v2.typ}")

        elif ctx.MUL():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.mul_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.mul_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.n+=1
                self.gen.int_to_float(self.n, v1.name)
                self.gen.mul_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1                

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.n+=1
                self.gen.int_to_float(self.n, v2.name)
                self.gen.mul_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=1

            else:
                raise TypeError(f"Unsupported type for mul: {v1.typ}, {v2.typ}")
             

        
    
        