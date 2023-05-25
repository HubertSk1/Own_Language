from antlr4 import *
from MutterspracheLexer import MutterspracheLexer
from MutterspracheParser import MutterspracheParser
from antlr4.tree.Trees import Trees


def main():
    # Create an input stream from your sample input code
    with open("PlikTestowy.txt", "r") as file:
        input_code = file.read()
    input_stream = InputStream(input_code)

    # Create a lexer instance
    lexer = MutterspracheLexer(input_stream)

    # Get all the tokens from the lexer
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # Print all the tokens
    for token in token_stream.getTokens(start = 0, stop= 1):
        print(token)
    
    # Create a parser instance
    parser = MutterspracheParser(token_stream)

    # Start parsing from the 'prog' rule (or whatever your start rule is)
    tree = parser.prog()

    # getting names of rules from parser
    rule_names = parser.ruleNames

    # printing parse tree
    print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main()