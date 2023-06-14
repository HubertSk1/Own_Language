from MY_LANGListener import MY_LANGListener
from LLVMGenerator import LLVMGenerator
from MY_LANGParser import MY_LANGParser
from copy import copy

class MY_Lang_Base_Error(Exception):
    def __init__(self,message):
        self.message= message

class My_Lang_Type_Exception(MY_Lang_Base_Error):
    def __init__(self,message):
        super().__init__(message)

class MY_Lang_Override_Exception(MY_Lang_Base_Error):
    def __init__(self,message):
        super().__init__(message)

class MY_LANG_Undefined_Exception(MY_Lang_Base_Error):
    def __init__(self,message):
        super().__init__(message)

class MY_LANG_Not_Supported_Arguments_type(MY_Lang_Base_Error):
    def __init__(self,message):
        super().__init__(message)


class Value:
    def __init__(self, name_of_variable, type_of_variable, size=None):
        self.name = name_of_variable
        self.typ = type_of_variable
        self.size = size
    def __str__(self):
        return f"Variable {self.name} of type {self.typ}"

class name_space:
    def __init__(self,consist_of_namespaces,name="None"):
        self.name = name
        self.consist_of_namespaces=consist_of_namespaces
        self.variables = self.get_prev_variables()
    def get_prev_variables(self):
        if self.consist_of_namespaces:
            return copy(self.consist_of_namespaces[-1].variables)
        else: 
            return dict()

class MyListener(MY_LANGListener):
    def __init__(self):
        self.stack = []
        self.current_namespace=name_space([],"global")
        self.n = 1
        self.gen = LLVMGenerator()
        self.functions=[]
    def print_stack(self):
        for ele in self.stack:
            print(ele)

    def print_variables(self):
        for var in self.current_namespace.variables:
            print(self.current_namespace.variables[var])
        print(self.current_namespace.variables.keys())

    def exitProg(self, ctx):
        self.print_variables()
        print(self.functions)
        pass
    
    def exitStatements(self, ctx):
        self.gen.clear_buffer()

    def exitFunction_header(self, ctx):
        if ctx.ID().getText() not in self.functions:
            types=[]
            types_name=[]
            names=[]
            ctx_arg_list = ctx.arg_list()
            for typ in ctx_arg_list.typ():
                types_name.append(typ.getText())
                if typ.getText() =="INT":
                    types.append("i32")
                elif typ.getText() =="REAL":
                    types.append("float")
                else :
                    raise MY_LANG_Not_Supported_Arguments_type(f"Unsupported  type as function argument")
            for name in ctx_arg_list.ID():
                names.append(name.getText())
            args=""
            for i in range(len(names)):
                args+=types[i]+ " %" + names[i] + ',' 
            args=args[0:-1]
            self.gen.function_start(ctx.ID().getText(),args)
            for i in range(len(names)):
                self.gen.alloca(f"%{self.n}", types[i])
                self.gen.asign_i32(f"%{self.n}",f"%{names[i]}")
                self.current_namespace.variables[names[i]]=Value(f'%{self.n}',types_name[i])
                self.n+=1
            self.functions.append(ctx.ID().getText())
        else:
            raise MY_Lang_Override_Exception(f"Cant override function {ctx.ID().getText()}")

    def enterDefine(self,ctx):
        prev_namespace=copy(self.current_namespace)
        prev_namespace.consist_of_namespaces.append(prev_namespace)
        self.current_namespace=name_space(prev_namespace.consist_of_namespaces)
        self.n=1
        pass

    def exitDefine(self, ctx):
        print("secend")
        ctx = ctx.end_function()
        ID = ctx.ID().getText()

        if ID in self.current_namespace.variables.keys():
            my_name = self.current_namespace.variables[ID].name
            if self.current_namespace.variables[ID].typ == "INT":
                self.gen.load_int(self.n,self.current_namespace.variables[ID].name)
            elif self.current_namespace.variables[ID].typ == "REAL":
                self.gen.load_real(self.n,self.current_namespace.variables[ID].name)
        else :
            raise MY_LANG_Undefined_Exception(f"variable {ID} undefined")
        
        self.gen.function_end(f"{self.n}")
        self.n=1
        self.print_variables()
        self.current_namespace=self.current_namespace.consist_of_namespaces[-1]
        
    def exitAssign(self, ctx):
        v = self.stack.pop()
        if ctx.ID():
            var_name = ctx.ID().getText()
            if v.typ=="INT":
                if var_name in self.current_namespace.variables:
                    name = self.current_namespace.variables[var_name].name    
                    self.gen.asign_i32(name,v.name)
                else: 
                    if self.current_namespace.name=="global":
                        self.current_namespace.variables[var_name]=Value(f"@{var_name}","INT")
                        self.gen.global_var(f"@{var_name}","i32", 0)
                        self.gen.asign_i32(f"@{var_name}",v.name)
                    else: 
                        self.current_namespace.variables[var_name]=Value(f"%{self.n}","INT")
                        self.gen.alloca(f"%{self.n}","i32")
                        self.gen.asign_i32(f"%{self.n}",v.name)
                        self.n+=1

            elif v.typ == "REAL":
                if var_name in self.current_namespace.variables:
                    name = self.current_namespace.variables[var_name].name        
                    self.gen.asign_float(name,v.name)
                else:
                    if self.current_namespace.name=="global":
                        self.current_namespace.variables[var_name] = Value(f"@{var_name}", "REAL")
                        self.gen.global_var(f"@{var_name}", "float", 0.00)
                        self.gen.asign_float(f"@{var_name}", v.name)
                    else:
                        self.current_namespace.variables[var_name] = Value(f"%{self.n}", "REAL")
                        self.gen.alloca(f"%{self.n}", "float")
                        self.gen.asign_float(f"%{self.n}", v.name)
                        self.n+=1

    def exitPrint(self, ctx):
        v = self.stack.pop()
        if v.typ == "INT":
            self.gen.print_i32(v.name,self.n)
        elif v.typ == "REAL":
            self.gen.printf_float(v.name,self.n)
        self.n+=1

    def exitRead(self, ctx):
        var_name = ctx.ID().getText()
        id = self.current_namespace.variables[var_name].name
        if self.current_namespace.variables[var_name].typ == "INT":
            self.gen.scanf_i32(id,self.n)
        elif self.current_namespace.variables[var_name].typ == "REAL":
            self.gen.scanf_float(id,self.n)

    def exitExpr(self, ctx):
        if ctx.INT():
            self.stack.append(Value(ctx.INT().getText(),"INT"))

        elif ctx.REAL():
            self.stack.append(Value(ctx.REAL().getText()+"0","REAL"))

        elif ctx.ID():
            if ctx.ID().getText() in self.current_namespace.variables.keys():
                if self.current_namespace.variables[ctx.ID().getText()].typ=="INT":
                    self.gen.load_int(self.n,self.current_namespace.variables[ctx.ID().getText()].name)
                elif self.current_namespace.variables[ctx.ID().getText()].typ=="REAL":
                    self.gen.load_real(self.n,self.current_namespace.variables[ctx.ID().getText()].name)
                self.stack.append(Value(f"%{self.n}",self.current_namespace.variables[ctx.ID().getText()].typ))
                self.n+=1
        elif ctx.ADD():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.add_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.add_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))
                self.n+=1

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.gen.int_to_float(self.n, v1.name)
                self.gen.add_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.gen.int_to_float(self.n, v2.name)
                self.gen.add_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2

            else:
                raise TypeError(f"Unsupported type for add: {v1.typ}, {v2.typ}")
            

        elif ctx.SUB():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.sub_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.sub_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))
                self.n+=1

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.gen.int_to_float(self.n, v1.name)
                self.gen.sub_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.gen.int_to_float(self.n, v2.name)
                self.gen.sub_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2

            else:
                raise TypeError(f"Unsupported type for sub: {v1.typ}, {v2.typ}")

        elif ctx.DIV():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.div_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.div_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))
                self.n+=1

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.gen.int_to_float(self.n, v1.name)
                self.gen.div_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.gen.int_to_float(self.n, v2.name)
                self.gen.div_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2
            else:
                raise TypeError(f"Unsupported type for div: {v1.typ}, {v2.typ}")

        elif ctx.MUL():
            v1 = self.stack.pop()
            v2 = self.stack.pop()

            if v1.typ == "INT" and v2.typ == "INT":
                self.gen.mul_i32(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "INT"))
                self.n+=1

            elif v1.typ == "REAL" and v2.typ == "REAL":
                self.gen.mul_float(self.n, v1.name, v2.name)
                self.stack.append(Value(f"%{self.n}", "REAL"))
                self.n+=1

            elif v1.typ == "INT" and v2.typ == "REAL":
                self.gen.int_to_float(self.n, v1.name)
                self.gen.mul_float(self.n+1, f"%{self.n}", v2.name)
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2                

            elif v1.typ == "REAL" and v2.typ == "INT":
                self.gen.int_to_float(self.n, v2.name)
                self.gen.mul_float(self.n+1, v1.name, f"%{self.n}")
                self.stack.append(Value(f"%{self.n+1}", "REAL"))
                self.n+=2
            else:
                raise TypeError(f"Unsupported type for mul: {v1.typ}, {v2.typ}")