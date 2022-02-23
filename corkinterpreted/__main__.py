from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


def main():
    while True:
        text = input('cork> ')
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()

        # Parse the tokens into an AST
        parser = Parser(tokens, text)
        tree = parser.parse()
        error = parser.error

        # Did we get an error from the lexer/parser? If so, display it
        if error:
            print(error)

        # Interpret the tree (if we have one), and display the value
        elif tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            error = interpreter.error

            # If we have an error, show it
            if error:
                print(error)
            elif value:
                print(value)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting cork...')
