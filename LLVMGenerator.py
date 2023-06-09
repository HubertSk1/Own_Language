
class LLVMGenerator():
    def __init__(self):
        self.main_text = ""
        self.buffer= ""
        self.header_text = ""
        self.declare_print_f = "@print_f = private unnamed_addr constant [4 x i8] c\"%f\\0A\\00\", align 1\n"
        self.declare_scan_f = "@scan_f = private unnamed_addr constant [3 x i8] c\"%f\\00\", align 1\n"

    def print_main_text(self):
        text = ''
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@print_f = private unnamed_addr constant [4 x i8] c\"%f\\0A\\00\", align 1\n"
        text += "@scan_f = private unnamed_addr constant [3 x i8] c\"%f\\00\", align 1\n"
        text += "@.stri = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\", align 1\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\", align 1\n"
        # text += "@.strd = private unnamed_addr constant [4 x i8] c\"%d\0A\00\", align 1\n"
        text += "@.strlf = private unnamed_addr constant [4 x i8] c\"%lf\\00\", align 1\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\", align 1\n"
        text += "@.strsf = private unnamed_addr constant [3 x i8] c\"%s\\00\", align 1\n"
        text += "@.strsfn = private unnamed_addr constant [6 x i8] c\"%[^\\0A]\\00\", align 1\n"
        text += self.header_text
        text += "define i32 @main() #0{\n"
        text += self.main_text 
        text += "ret i32 0 }\n"
        # print(self.buffer)
        return text

    def add_i32(self,id,val1,val2):
        self.buffer += f"%{id} = add i32 {val1},{val2}\n"

    def add_double(self, id, val1, val2):
        self.buffer += f"%{id} = fadd double {val1}, {val2}\n"

    def sub_i32(self,id,val1,val2):
        self.buffer += f"%{id} = sub i32 {val1},{val2}\n"

    def sub_double(self, id, val1, val2):
        self.buffer += f"%{id} = fsub double {val1}, {val2}\n"
    
    def div_i32(self, id, val1, val2):
        self.buffer += f"%{id} = sdiv i32 {val1}, {val2}\n"

    def div_double(self, id, val1, val2):
        self.buffer += f"%{id} = fdiv double {val1}, {val2}\n"

    def mul_i32(self,id,val1,val2):
        self.buffer += f"%{id} = mul i32 {val1},{val2}\n"

    def mul_double(self, id, val1, val2):
        self.buffer += f"%{id} = fmul double {val1}, {val2}\n"

    def print_i32(self,id,placeholder):
        self.buffer += f"call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 {id})\n"

    def printf_double(self, id, placeholder):
        self.buffer += f"%{placeholder} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double {id})\n"
        # "%"+reg+" = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %"+(reg-1)+")\n"
        # raise NotImplementedError()
    def scanf_i32(self, id,placeholder):
        self.buffer += f"%{placeholder} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* {id})\n"
        # raise NotImplementedError()
    def scanf_double(self, id, placeholder):
        self.buffer += f"%{placeholder}  = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strlf, i32 0, i32 0), double* {id})\n"
        # raise NotImplementedError()
    def asign_i32(self,id,value):
        self.buffer += f"store i32 {value}, i32* {id}\n"
    
    def asign_double(self, id, value):
        self.buffer += f"store double {value}, double* {id}\n"

    def alloca(self,id,type):
        self.buffer += f"{id} = alloca {type}\n"

    def int_to_double(self, id, val):
        self.buffer += f"%{id} = sitofp i32 {val} to double\n"

    def load_int(self,placeholder,id):
        self.buffer += f"%{placeholder}= load i32, i32* {id}\n"

    def load_real(self,placeholder,id):
        self.buffer += f"%{placeholder}= load double, double* {id}\n"

    def function_start(self,id,args):
        self.buffer = f"define i32 @{id}({args}) nounwind "+"{ \n"

    def compare(self,id,type,operation,a,b):
        self.buffer+=f"{id} =icmp {operation} {type} {a},{b}\n"

    def cond_jump(self,number):
        self.buffer+=f"br i1 %cmp{number}, label %iftrue{number}, label %iffalse{number}\n"

    def loop_jump(self,number):
        self.buffer+=f"br i1 %cmp{number}, label %end{number}, label %loop{number}\n"

    def function_end(self,id):
        self.buffer += f"ret i32 {id}\n"; 
        self.buffer += "}\n"
        self.header_text += self.buffer
        self.buffer = ""

    def global_var(self,var_name,typ,def_value):
        self.header_text+=f"{var_name} = global {typ} {def_value}\n"

    def call_fun(self,n,name,args):
        self.buffer+=f"%{n} = call i32 {name}({args})\n"
    def jump_to_label(self,label):
        self.buffer+=f"br label {label}\n"
    def create_label(self,label,number):
        self.buffer+=f"{label}{number}:\n"

    def create_structure(self,name,args):
        self.header_text+=f"%{name} = type"+"{\n"f"{args}"+"}\n"
        
    def clear_buffer(self):
        self.main_text+=self.buffer
    
    def put_value_to_structure(self,number,fieldname,structurename,number_of_field,value_to_store,type_of_value,allocaled_name):
        self.buffer+=f"%{fieldname}_{number} = getelementptr %{structurename}, %{structurename}* {allocaled_name}, i32 0, i32 {number_of_field}\n"
        self.buffer+=f"store {type_of_value} {value_to_store}, {type_of_value}* %{fieldname}_{number}\n"

    def get_structure_element(self,number,structure_type,field_number,structure_name):
        self.buffer+=f"%{number} = getelementptr {structure_type}, {structure_type}* {structure_name}, i32 0, i32 {field_number}\n"