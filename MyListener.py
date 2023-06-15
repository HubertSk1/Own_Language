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

class fun:
    def __init__(self,name,types):
        self.name = name
        self.types = types
class structure:
    def __init__(self,name,fields,types):
        self.name=name
        self.fields=fields
        self.types=types

class MyListener(MY_LANGListener):
    def __init__(self):
        self.stack = []
        self.current_namespace=name_space([],"global")
        self.n = 1
        self.gen = LLVMGenerator()
        self.functions=dict()
        self.blocknumber=0
        self.block_stack=[]
        self.structures=dict()

    def print_stack(self):
        for ele in self.stack:
            print(ele)

    def print_variables(self):
        for var in self.current_namespace.variables:
            print(self.current_namespace.variables[var])
        print(self.current_namespace.variables.keys())

    def exitProg(self, ctx):
        self.print_variables()
        pass
    
    def exitStatements(self, ctx):
        self.gen.clear_buffer()

    def exitFunction_header(self, ctx):
        if ctx.ID().getText() not in self.functions.keys():
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
                if types[i]=="i32":
                    self.gen.asign_i32(f"%{self.n}",f"%{names[i]}")
                elif types[i]=="float":
                    self.gen.asign_float(f"%{self.n}",f"%{names[i]}")
                self.current_namespace.variables[names[i]]=Value(f'%{self.n}',types_name[i])
                self.n+=1
            self.functions[ctx.ID().getText()]=fun(ctx.ID().getText(),types_name)
        else:
            raise MY_Lang_Override_Exception(f"Cant override function {ctx.ID().getText()}")

    def enterDefine(self,ctx):
        prev_namespace=copy(self.current_namespace)
        prev_namespace.consist_of_namespaces.append(prev_namespace)
        self.current_namespace=name_space(prev_namespace.consist_of_namespaces)
        self.n=1
        pass

    def exitDefine(self, ctx):
        ctx = ctx.end_function()
        ID = ctx.ID().getText()

        if ID in self.current_namespace.variables.keys():
            my_name = self.current_namespace.variables[ID].name
            if self.current_namespace.variables[ID].typ == "INT":
                self.gen.load_int(self.n,my_name)
            elif self.current_namespace.variables[ID].typ == "REAL":
                self.gen.load_real(self.n,my_name)
        else :
            raise MY_LANG_Undefined_Exception(f"variable {ID} undefined")
        
        self.gen.function_end(f"%{self.n}")
        self.n=1
        self.current_namespace=self.current_namespace.consist_of_namespaces[-1]
        
    def exitCall_function(self, ctx):
        if ctx.ID().getText() in self.functions.keys():
            types_of_vars = self.functions[ctx.ID().getText()].types
            txt=""
            self.stack.reverse()
            for i in range (0,len(ctx.expr())):
                var=self.stack.pop()
                if var.typ != types_of_vars[i]:
                    raise MY_LANG_Not_Supported_Arguments_type("Wrong types for function")
                if var.typ =="INT":
                    txt+="i32 "
                if var.typ == "REAL":
                    txt+="float "
                txt+= var.name 
                txt+=','
            txt=txt[0:-1]
            self.gen.call_fun(self.n,f"@{ctx.ID().getText()}",txt)
        else:
            raise MY_LANG_Undefined_Exception("function undefined")
        
    def enterConditional_header(self,ctx):
        self.blocknumber+=1
        self.block_stack.append(self.blocknumber)

    def exitConditional_header(self,ctx):
        self.gen.cond_jump(self.block_stack[-1])
        self.gen.create_label("iftrue",self.block_stack[-1])

    def enterElse_part(self,ctx):
        self.gen.jump_to_label(f"%end{self.block_stack[-1]}")

    def exitElse_part(self,ctx):
        self.gen.create_label("iffalse",self.block_stack[-1])
    
    def exitConditional_stat(self, ctx):
        self.gen.jump_to_label(f"%end{self.block_stack[-1]}")
        self.gen.create_label("end",self.block_stack[-1])
        self.block_stack.pop()

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
            elif v.typ in self.structures.keys():
                    types=["i32" if x =="INT" else "float" for x in self.structures[v.typ].types ]
                    self.gen.alloca(f"%{self.n}",f"%{v.typ}")
                    self.stack.reverse()
                    for i in range(len(types)):
                        value_of_field=self.stack.pop()
                        self.gen.put_value_to_structure(self.n,self.structures[v.typ].fields[i],v.typ,i,value_of_field.name,types[i],f"%{self.n}")
                    self.current_namespace.variables[ctx.ID().getText()]=Value(f"%{self.n}",f"{v.typ}")
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

    def enterLoop_header(self,ctx):
        self.blocknumber+=1
        self.block_stack.append(self.blocknumber)

    def enterLoop(self,ctx):
        prev_namespace=copy(self.current_namespace)
        prev_namespace.consist_of_namespaces.append(prev_namespace)
        self.current_namespace=name_space(prev_namespace.consist_of_namespaces)

    def exitLoop(self,ctx):
        self.block_stack.pop()
        self.current_namespace=self.current_namespace.consist_of_namespaces[-1]

    def exitLoop_header(self,ctx):
        rep=self.stack.pop()
        if rep.typ != "INT":
            raise MY_LANG_Not_Supported_Arguments_type("Number of repetitions must be INT type")

        self.gen.alloca(f"%reps{self.block_stack[-1]}","i32")
        self.gen.asign_i32(f"%reps{self.block_stack[-1]}",rep.name)

        self.gen.alloca(f"%counter{self.block_stack[-1]}","i32")
        self.gen.asign_i32(f"%counter{self.block_stack[-1]}",0)
        self.gen.jump_to_label(f"%loop{self.block_stack[-1]}")
        self.gen.create_label(f"loop",self.block_stack[-1])

        self.gen.load_int(self.n,f"%counter{self.block_stack[-1]}")
        self.gen.add_i32(f"incrementedcounter{self.block_stack[-1]}",f"%{self.n}",1)
        self.gen.asign_i32(f"%counter{self.block_stack[-1]}",f"%incrementedcounter{self.block_stack[-1]}")
        self.n+=1

    def exitLoop_end(self,ctx):
        self.gen.load_int(f"to_compare{self.block_stack[-1]}",f"%counter{self.block_stack[-1]}")
        self.gen.load_int(f"to_compare{self.block_stack[-1]}_{self.block_stack[-1]}",f"%reps{self.block_stack[-1]}")
        self.gen.compare(f"%cmp{self.block_stack[-1]}","i32","eq",f"%to_compare{self.block_stack[-1]}",f"%to_compare{self.block_stack[-1]}_{self.block_stack[-1]}")
        self.gen.loop_jump(self.block_stack[-1])
        self.gen.create_label("end",self.block_stack[-1])

    def exitStruct(self,ctx):
        text=""
        types=[]
        names=[]
        for t in ctx.arg_list().typ():
            if t.getText()=="INT":
                types.append("INT")
                text+=f"i32,\n"
            elif t.getText()=="REAL":
                types.append("REAL")
                text+=f"float,\n"
            else:
                raise MY_LANG_Not_Supported_Arguments_type("STRUCT only support REAL and INT for now")
        text=text[0:-2]
        for t in ctx.arg_list().ID():
            names.append(t.getText())
        
        self.gen.create_structure(ctx.ID().getText(),text)
        self.structures[ctx.ID().getText()]=structure(f"%{ctx.ID().getText()}",names,types)



    def exitBool_stat(self, ctx):
        var1=self.stack.pop()
        var2=self.stack.pop()
        if var1.typ != var2.typ:
            raise MY_LANG_Not_Supported_Arguments_type("Types to be  compared must be the same")
        if var1.typ not in ["REAL","INT"]:
            raise MY_LANG_Not_Supported_Arguments_type("Comparison only of REAL and INT is possible")
        typ = ""
        if var1.typ =="REAL":
            typ="float"
        elif var1.typ =="INT":
            typ="i32"
        operation=""
        self.stack.append(Value(f"%cmp{self.blocknumber}","BOOL"))
        if ctx.GREATER():
            operation="sgt"
        elif ctx.LOWER():
            operation="slt"
        elif ctx.EQUAL():
            operation="eq"
        self.gen.compare(f"%cmp{self.blocknumber}",typ,operation,var1.name,var2.name)
        
    def exitExpr(self, ctx):
        if ctx.INT():
            self.stack.append(Value(ctx.INT().getText(),"INT"))

        elif ctx.REAL():
            self.stack.append(Value(ctx.REAL().getText()+"0","REAL"))

        elif ctx.call_function():
            self.stack.append(Value(f"%{self.n}","INT"))

        elif ctx.create_structure():
            if ctx.create_structure().ID().getText() in self.structures.keys():
                self.stack.append(Value(f"%{self.n}",f"{ctx.create_structure().ID().getText()}"))
        
        elif ctx.part_structure():
            ID1 = ctx.part_structure().ID()[0].getText()
            ID2 = ctx.part_structure().ID()[1].getText()
            if ID1 in self.current_namespace.variables.keys():
                this_structure = self.current_namespace.variables[ID1]
                fields = self.structures[this_structure.typ].fields
                types = self.structures[this_structure.typ].types
                err=1
                for index,field in enumerate(fields):
                    if field == ID2:
                        self.gen.get_structure_element(self.n,self.structures[this_structure.typ].name,index)
                        self.stack.append(Value(f"%{self.n}",types[index]))
                        self.n+=1
                        err=0
                if err==1:
                    raise MY_LANG_Undefined_Exception("wrong field for structure")
                
            else :
                raise MY_LANG_Undefined_Exception("this structure is undefined in this scope")



        elif ctx.ID():
            if ctx.ID().getText() in self.current_namespace.variables.keys():
                if self.current_namespace.variables[ctx.ID().getText()].typ=="INT":
                    self.gen.load_int(self.n,self.current_namespace.variables[ctx.ID().getText()].name)
                elif self.current_namespace.variables[ctx.ID().getText()].typ=="REAL":
                    self.gen.load_real(self.n,self.current_namespace.variables[ctx.ID().getText()].name)
                self.stack.append(Value(f"%{self.n}",self.current_namespace.variables[ctx.ID().getText()].typ))
                self.n+=1
            else :
                raise MY_LANG_Undefined_Exception(f"Variable {ctx.ID().getText()} is undefinded in this scope (or is a structure)")

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