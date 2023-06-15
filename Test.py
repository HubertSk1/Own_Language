from antlr4 import *
import antlr4
from MY_LANGLexer import MY_LANGLexer
from MY_LANGParser import MY_LANGParser
from antlr4.tree.Trees import Trees
from MyListener import MyListener

from llvmlite import ir
from llvmlite import binding

import subprocess

def main():

    # Open input file
    with open("Testy/Ify.txt", "r") as file:
        input_code = file.read()
    input_stream = InputStream(input_code)

    # Create a lexer instance
    lexer = MY_LANGLexer(input_stream)

    # Get all the tokens from the lexer
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # # Print all the tokens
    # for token in token_stream.getTokens(start = 0, stop= 10000):
    #     print(token)
    
    # Create a parser instance
    parser = MY_LANGParser(token_stream)

    # Start parsing from the 'prog' rule 
    tree = parser.prog()


    for node in tree.children:
        if type(node) is antlr4.tree.Tree.ErrorNodeImpl:
            print(">>>Blad generacji kodu")
            return

    # printing parse tree
    print(Trees.toStringTree(tree, None, parser))

    printer = MyListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    whole_program_LLVM = printer.gen.print_main_text()
    print(whole_program_LLVM)

    def check_llvm_ir(llvm_ir):
    # Tworzenie kontekstu i modułu LLVM
        context = ir.Context()
        module = ir.Module(context)
        
        try:
            # Wczytywanie kodu LLVM IR 
            module = binding.parse_assembly(llvm_ir)
            
            # Sprawdzanie poprawności
            module.verify()
            print("Kod LLVM IR jest poprawny.")
            
        except Exception as e:
            print("Błąd w kodzie LLVM IR:")
            print(str(e))
    
    # check_llvm_ir(whole_program_LLVM)

    # # Inicjalizacja LLVM
    # binding.initialize()
    # binding.initialize_native_target()
    # binding.initialize_native_asmprinter()

    # def optimize_and_compile_llvm_ir(llvm_ir_code):
    #     # Tworzenie kontekstu modułu LLVM
    #     context = ir.Context()
    #     module = ir.Module(context)

    #      # Parsowanie kodu LLVM IR
    #     module = binding.parse_assembly(llvm_ir_code)

    #     # Tworzenie maszyny celu
    #     target_machine = binding.Target.from_default_triple().create_target_machine()

    #     # Tworzenie silnika optymalizacji
    #     pass_manager_builder = binding.create_pass_manager_builder()
    #     pass_manager_builder.opt_level = 3
    #     pass_manager = binding.create_module_pass_manager()

    #     # Dodawanie optymalizacji
    #     pass_manager_builder.populate(pass_manager)

    #     # Optymalizacja modułu
    #     pass_manager.run(module)

    #     # Kompilacja modułu do kodu maszynowego
    #     machine_module = target_machine.emit_object(module)

    #     # Zwracanie kodu maszynowego jako ciągu bajtów
    #     return bytes(machine_module)


    # machine_code = optimize_and_compile_llvm_ir(whole_program_LLVM)
    
    # #print(machine_code)

    # # Zapisz kod maszynowy do pliku tymczasowego
    # filename = 'temp.bin'
    # with open(filename, 'wb') as f:
    #     f.write(machine_code)

    # # Wywołaj program z plikiem binarnym
    # #subprocess.Popen(filename, shell=True)

    # def read_binary_file(file_path):
    #     with open(file_path, 'rb') as file:
    #         binary_data = file.read()
    #     return binary_data

    # def print_hex(binary_data):
    #     for byte in binary_data:
    #         print(format(byte, '02x'), end=' ')
    #     print()

    # # Przykładowe użycie:
    # file_path = 'temp.bin'
    # binary_data = read_binary_file(file_path)
    # #print_hex(binary_data)

    # # Usuń plik tymczasowy
    # #subprocess.call(['del', filename], shell=True)
       

if __name__ == '__main__':
    main()