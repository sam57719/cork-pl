from exceptions import InvalidSyntax
from nodes import *
from tokens import TokenType
from decorators import check_for_instance_error


class Parser:
    def __init__(self, tokens, text):
        self.tokens = iter(tokens)
        self.text = text
        self.current_token = None
        self.error = None

        self.advance()

    def advance(self):
        try:
            self.current_token, self.error = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        self.error = InvalidSyntax()

    def parse(self):
        if self.current_token is None:
            return None, self.error

        result = self.expr()

        # If we reach here and we haven't processed all the tokens, then there must be a syntax error
        if self.current_token is not None:
            self.raise_error()

        return result, self.error

    @check_for_instance_error(method_has_return=True)
    def expr(self):
        """
        Arithmetic Expression
        expr    : term ((PLUS|MINUS) term)*
        """

        if self.current_token is None:
            self.raise_error()

        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())

            # Must be Minus token if we hit this else block
            else:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    @check_for_instance_error(method_has_return=True)
    def term(self):
        """
        Arithmetic Term
        term    : factor ((MULTIPLY|DIVIDE|FLOOR|MOD) factor)*
        """

        if self.current_token is None:
            self.raise_error()

        result = self.factor()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE,
                                                                             TokenType.FLOOR, TokenType.MOD):

            match self.current_token.type:
                case TokenType.MULTIPLY:
                    self.advance()
                    result = MultiplyNode(result, self.factor())
                case TokenType.DIVIDE:
                    self.advance()
                    result = DivideNode(result, self.factor())

                case TokenType.FLOOR:
                    self.advance()
                    result = FloorNode(result, self.factor())

                case TokenType.MOD:
                    self.advance()
                    result = ModNode(result, self.factor())

        return result

    @check_for_instance_error(method_has_return=True)
    def factor(self):
        """
        Arithmetic Factor
        factor      : (PLUS|MINUS) factor
                    : power
        """

        if self.current_token is None:
            self.raise_error()

        token = self.current_token

        match token.type:
            case TokenType.PLUS:
                self.advance()
                return PlusNode(self.factor())
            case TokenType.MINUS:
                self.advance()
                return MinusNode(self.factor())

        return self.power()

    @check_for_instance_error(method_has_return=True)
    def power(self):
        """
        Arithmetic Power
        power       : atom (POWER factor)*
        """

        if self.current_token is None:
            self.raise_error()

        result = self.atom()

        while self.current_token is not None and self.current_token.type == TokenType.POWER:
            self.advance()
            result = PowerNode(result, self.factor())

        return result

    @check_for_instance_error(method_has_return=True)
    def atom(self):
        """
        Atomic Level
        atom        : number
                    : LPAREN expr RPAREN
        """

        if self.current_token is None:
            self.raise_error()

        match self.current_token.type:
            case TokenType.NUMBER:
                return self.number()

            case TokenType.LPAREN:
                self.advance()
                result = self.expr()

                if self.current_token is None or self.current_token.type != TokenType.RPAREN:
                    self.raise_error()

                self.advance()
                return result

        self.raise_error()

    @check_for_instance_error(method_has_return=True)
    def number(self):
        """
        Arithmetic Number
        number  : INTEGER|FLOAT
        """

        if self.current_token is None:
            self.raise_error()

        token = self.current_token
        self.advance()

        return NumberNode(token.value)


