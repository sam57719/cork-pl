class Error:
    def __init__(self, details=None):
        self.error_name = self.__class__.__name__
        self.details = details

    def __repr__(self):
        result = f'{self.error_name}'

        # Add the details if specified
        if self.details:
            result += f': {self.details}'

        return result


class IllegalCharacter(Error):
    def __init__(self, character=None):
        details = f'Invalid character \'{character}\'' if character else None
        super().__init__(details)


class InvalidSyntax(Error):
    def __init__(self):
        super().__init__()


# noinspection PyShadowingBuiltins
class ZeroDivisionError(Error):
    def __init__(self):
        details = 'Cannot divide by zero'
        super().__init__(details)


class ComplexNumbersNotSupported(Error):
    def __init__(self):
        details = f'Complex numbers are not supported'
        super().__init__(details)


# noinspection PyShadowingBuiltins
class NotImplementedError(Error):
    def __init__(self, method):
        details = f'{method} not implemented properly - no visit_ method defined'
        super().__init__(details)
