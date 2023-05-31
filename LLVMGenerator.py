
class LLVMGenerator():
    def __init__(self):
        self.main_text = ""

    def print_main_text(self):
        print(self.main_text)

    def add_i32(self,id,val1,val2):
        self.main_text += f"%{id} = add i32 {val1},{val2}\n"

    def sub_i32(self,id,val1,val2):
        self.main_text += f"%{id} = sub i32 {val1},{val2}\n"

    def mul_i32(self,id,val1,val2):
        self.main_text += f"%{id} = mul i32 {val1},{val2}\n"

    def print_i32(self,id,placeholder):
        self.main_text += f"%{placeholder} = load i32, i32* {id}\n"
        self.main_text += f"call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), i32 %{placeholder})\n"

    def asign_i32(self,id,value):
        self.main_text += f"store i32 {value}, i32* {id}\n"

    def alloca(self,id,type):
        self.main_text += f"{id} = alloca {type}\n"
