from dataclasses import dataclass
from exceptions import ComplexNumbersNotSupported, ZeroDivisionError
from fractions import Fraction


@dataclass(eq=True)
class Number:
    value: Fraction

    def __repr__(self):
        return f'{self.value if "/" not in str(self.value) else float(self.value)}'

    def __add__(self, other):
        match other:
            case Number():
                return Number(self.value + other.value), None
            case _:
                return None, None

    def __sub__(self, other):
        match other:
            case Number():
                return Number(self.value - other.value), None
            case _:
                return None, None

    def __mul__(self, other):
        match other:
            case Number():
                return Number(self.value * other.value), None
            case _:
                return None, None

    def __truediv__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                return None, ZeroDivisionError()
            case Number():
                return Number(self.value / other.value), None
            case _:
                return None, None

    def __floordiv__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                return None, ZeroDivisionError()
            case Number():
                return Number(self.value // other.value), None
            case _:
                return None, None

    def __mod__(self, other):
        match other:
            # Catch division by 0
            case Number(0):
                return None, ZeroDivisionError()
            case Number():
                return Number(self.value % other.value), None
            case _:
                return None, None

    def __pos__(self):
        return Number(+self.value), None

    def __neg__(self):
        return Number(-self.value), None

    def __pow__(self, other):
        match other:
            case Number() if self.value >= 0:
                return Number(self.value ** other.value), None
            case _ if self.value < 0:
                return None, ComplexNumbersNotSupported()
            case _:
                return None, None
