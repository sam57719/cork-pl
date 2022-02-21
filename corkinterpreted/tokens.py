from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = 'NUMBER'
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    LPAREN = '('
    RPAREN = ')'
    FLOOR = '//'
    MOD = '%'
    POWER = '^'


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f':{self.value}' if self.value is not None else '')
