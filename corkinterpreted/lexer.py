from tokens import TokenType, Token
from exceptions import IllegalCharacter
from fractions import Fraction

SINGLE_CHAR_TOKEN_TYPES = [t.value for t in TokenType if t.value is not None and len(t.value) == 1]


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.text_string = text
        self.current_char = None
        self.pos = -1

        self.advance()

    def advance(self):
        """ Gets the next character from the input string """
        try:
            self.pos += 1
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        """ Generates Tokens from the input string """
        while self.current_char is not None:
            current_char = self.current_char

            # Ignore whitespace
            if self.current_char.isspace():
                self.advance()

            # Retrieve and build the full number as one token
            elif self.current_char.isdigit() or self.current_char == '.':
                yield self._generate_number(), None

            # Check if this '/' is part of a '//' operation
            elif self.current_char == '/':
                yield self._make_divide_or_floor(), None

            # Get any single character tokens that haven't already been processed
            elif self.current_char in SINGLE_CHAR_TOKEN_TYPES:
                self.advance()
                yield Token(TokenType(current_char)), None

            else:
                yield None, IllegalCharacter(current_char)

    def _generate_number(self):
        """ Builds a number """
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            # Only allow one decimal point per number
            if self.current_char == '.' and number_str.count('.') == 1:
                break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        # Return Number Token
        return Token(TokenType.NUMBER, Fraction(number_str))

    def _make_divide_or_floor(self):
        """ Checks whether a '/' could be a '//' and returns either token """
        self.advance()

        # If the next char is also a divide, then this is a floor token
        if self.current_char == '/':
            self.advance()
            return Token(TokenType.FLOOR)

        return Token(TokenType.DIVIDE)





