from antlr4 import *
import antlr4
from MY_LANGLexer import MY_LANGLexer
from MY_LANGParser import MY_LANGParser
from antlr4.tree.Trees import Trees
from MyListener import MyListener

from llvmlite import ir
from llvmlite import binding

def main():

    # Open input file
    with open("Testy/PlikTestowy.txt", "r") as file:
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
    #print(whole_program_LLVM)

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
    
    check_llvm_ir(whole_program_LLVM)

   

if __name__ == '__main__':
    main()