class IllegalCharacterError(Exception):
    """ Raise when an Illegal character is found """
    def __init__(self, character):
        message = f'Illegal Character \'{character}\''
        super().__init__(message)


class InvalidSyntaxError(Exception):
    """ Raise when the syntax is invalid """
    def __init__(self):
        message = f'Invalid syntax'
        super().__init__(message)


class ZeroDivisionError(Exception):
    """ Raise when dividing by 0 """
    def __init__(self):
        message = f'Cannot divide by 0'
        super().__init__(message)


class ComplexNumbersNotSupported(Exception):
    """ Raise when a complex number is produced """
    def __init__(self):
        message = f'Complex numbers are not supported'
        super().__init__(message)


