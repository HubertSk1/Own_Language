from antlr4 import *
import antlr4
from MY_LANGLexer import MY_LANGLexer
from MY_LANGParser import MY_LANGParser
from antlr4.tree.Trees import Trees
from MyListener import MyListener

from llvmlite import ir
from llvmlite import binding

import subprocess

from ctypes import CFUNCTYPE, c_double, c_int, c_byte, POINTER

def main():

    # Open input file
    with open("Testy/loop.txt", "r") as file:
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
    
    def exec(module):
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        target = binding.Target.from_default_triple()
        target_machine = target.create_target_machine()

        backing_mod = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_mod, target_machine)

        mod = binding.parse_assembly(str(module))
        mod.verify()
        engine.add_module(mod)
        engine.finalize_object()
        engine.run_static_constructors()

        func_ptr = engine.get_function_address("main")

        cFunc = CFUNCTYPE(c_int, c_int, POINTER(c_byte))(func_ptr)
        cFunc(0, None)

    def compile(module, basename):
        binding.initialize()
        binding.initialize_native_asmprinter()
        binding.initialize_native_target()

        target = binding.Target.from_default_triple()
        target_machine = target.create_target_machine()

        mod = binding.parse_assembly(str(module))
        mod.verify()
        with open(f"{basename}.o", "wb") as o:
            o.write(target_machine.emit_object(mod))

# print(code)
# you can pass string or module generated from ir.builder
    exec(whole_program_LLVM)
    compile(whole_program_LLVM, "test_output")   

if __name__ == '__main__':
    main()