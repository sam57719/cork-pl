from dataclasses import dataclass
from exceptions import ComplexNumbersNotSupported, ZeroDivisionError

@dataclass(eq=True)
class Number:
    value: int

    def __repr__(self):
        return f'{self.value}'

    def __add__(self, other):
        match other:
            case Number():
                return self.value + other.value
            case _:
                return None

    def __sub__(self, other):
        match other:
            case Number():
                return self.value - other.value
            case _:
                return None

    def __mul__(self, other):
        match other:
            case Number():
                return self.value * other.value
            case _:
                return None

    def __truediv__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                raise ZeroDivisionError
            case Number():
                return self.value / other.value

    def __floordiv__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                raise ZeroDivisionError
            case Number():
                return self.value // other.value

    def __mod__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                raise ZeroDivisionError
            case Number():
                return self.value % other.value

    def __pos__(self):
        return self.value

    def __neg__(self):
        return -self.value

    def __pow__(self, other):
        match other:
            case Number() if self.value >= 0:
                return self.value ** other.value
            case _ if self.value < 0:
                raise ComplexNumbersNotSupported
            case _:
                return None
