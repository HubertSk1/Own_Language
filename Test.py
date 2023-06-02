from antlr4 import *
from MY_LANGLexer import MY_LANGLexer
from MY_LANGParser import MY_LANGParser
from antlr4.tree.Trees import Trees
from MyListener import MyListener

def main():

    # Open input file
    with open("Testy/MatrixAdd.txt", "r") as file:
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

    # printing parse tree
    print(Trees.toStringTree(tree, None, parser))

    printer = MyListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    whole_program_LLVM = printer.gen.print_main_text()
    # print(whole_program_LLVM)
if __name__ == '__main__':
    main()