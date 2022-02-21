from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


DEBUG = {
    'tree': False,
}


def main(debug=DEBUG):
    while True:

        try:
            text = input('cork> ')
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()

            # Parse the tokens into an AST
            parser = Parser(tokens, text)
            tree = parser.parse()

            if DEBUG['tree']:
                print(f'DEBUG {tree=}')

            # Interpret the tree (if we have one)
            if tree:
                interpreter = Interpreter()
                value = interpreter.visit(tree)
                print(value)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()

