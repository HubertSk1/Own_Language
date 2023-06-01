
class LLVMGenerator():
    def __init__(self):
        self.main_text = ""
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
        print(self.main_text)
        return text

    def add_i32(self,id,val1,val2):
        self.main_text += f"%{id} = add i32 {val1},{val2}\n"

    def add_float(self, id, val1, val2):
        self.main_text += f"%{id} = fadd float {val1}, {val2}\n"

    def sub_i32(self,id,val1,val2):
        self.main_text += f"%{id} = sub i32 {val1},{val2}\n"

    def sub_float(self, id, val1, val2):
        self.main_text += f"%{id} = fsub float {val1}, {val2}\n"
    
    def div_i32(self, id, val1, val2):
        self.main_text += f"%{id} = sdiv i32 {val1}, {val2}\n"

    def div_float(self, id, val1, val2):
        self.main_text += f"%{id} = fdiv float {val1}, {val2}\n"

    def mul_i32(self,id,val1,val2):
        self.main_text += f"%{id} = mul i32 {val1},{val2}\n"

    def mul_float(self, id, val1, val2):
        self.main_text += f"%{id} = fmul float {val1}, {val2}\n"

    def print_i32(self,id,placeholder):
        self.main_text += f"%{placeholder} = load i32, i32* {id}\n"
        self.main_text += f"call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), i32 %{placeholder})\n"

    def printf_float(self, id, placeholder):
        self.main_text += f"%{placeholder} = getelementptr inbounds ([4 x i8], [4 x i8]* @print_f, i32 0, i32 0)\n"
        self.main_text += f"call i32 (i8*, ...) @printf(i8* %{placeholder}, float {id})\n"

    def scanf_i32(self, id):
        self.main_text += f"{id} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scanformat, i32 0, i32 0), i32* {id})\n"
 
    def scanf_float(self, id):
        self.main_text += f"{id}  = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strlf, i32 0, i32 0), float* {id})\n"

    def asign_i32(self,id,value):
        self.main_text += f"store i32 {value}, i32* {id}\n"
    
    def asign_float(self, id, value):
        self.main_text += f"store float {value}, float* {id}\n"

    def alloca(self,id,type):
        self.main_text += f"{id} = alloca {type}\n"

    def int_to_float(self, id, val):
        self.main_text += f"%{id} = sitofp i32 {val} to float\n"

