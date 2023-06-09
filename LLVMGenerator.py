
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
        text += "@.stri = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\", align 1\n"
        text += "@.strd = private unnamed_addr constant [4 x i8] c\"%f\\0A\\00\", align 1\n"
        text += "@.strlf = private unnamed_addr constant [4 x i8] c\"%lf\\00\", align 1\n"
        text += "@.strs = private unnamed_addr constant [4 x i8] c\"%s\\0A\\00\", align 1\n"
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

    def add_float(self, id, val1, val2):
        self.buffer += f"%{id} = fadd float {val1}, {val2}\n"

    def sub_i32(self,id,val1,val2):
        self.buffer += f"%{id} = sub i32 {val1},{val2}\n"

    def sub_float(self, id, val1, val2):
        self.buffer += f"%{id} = fsub float {val1}, {val2}\n"
    
    def div_i32(self, id, val1, val2):
        self.buffer += f"%{id} = sdiv i32 {val1}, {val2}\n"

    def div_float(self, id, val1, val2):
        self.buffer += f"%{id} = fdiv float {val1}, {val2}\n"

    def mul_i32(self,id,val1,val2):
        self.buffer += f"%{id} = mul i32 {val1},{val2}\n"

    def mul_float(self, id, val1, val2):
        self.buffer += f"%{id} = fmul float {val1}, {val2}\n"

    def print_i32(self,id,placeholder):
        self.buffer += f"call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 {id})\n"

    def printf_float(self, id, placeholder):
        self.buffer += f"call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strd, i32 0, i32 0), float {id})\n"
        
        

    def scanf_i32(self, id,placeholder):
        self.buffer += f"%{placeholder} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.stri, i32 0, i32 0), i32* {id})\n"
 
    def scanf_float(self, id, placeholder):
        self.buffer += f"%{placeholder}  = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strlf, i32 0, i32 0), float* {id})\n"

    def asign_i32(self,id,value):
        self.buffer += f"store i32 {value}, i32* {id}\n"
    
    def asign_float(self, id, value):
        self.buffer += f"store float {value}, float* {id}\n"

    def alloca(self,id,type):
        self.buffer += f"{id} = alloca {type}\n"

    def int_to_float(self, id, val):
        self.buffer += f"%{id} = sitofp i32 {val} to float\n"

    def load_int(self,placeholder,id):
        self.buffer += f"%{placeholder}= load i32, i32* {id}\n"

    def load_real(self,placeholder,id):
        self.buffer += f"%{placeholder}= load float, float* {id}\n"

    def function_start(self,id):
        self.buffer = "define i32 @"+id+"() nounwind {\n"

    def function_end(self,id):
        self.buffer += "ret i32 %"+(id)+"\n"; 
        self.buffer += "}\n"
        self.header_text += self.buffer
        self.buffer = ""

    def global_var(self,var_name,typ,def_value):
        self.header_text+=f"{var_name} = global {typ} {def_value}\n"

    def exit_main(self):
        self.main_text=self.buffer
