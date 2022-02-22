import functools


def skip_if_error(func=None, error_attribute='error', method_has_return=True, error_return_value=None,
                  attribute_default_value=None):
    """
    skip_if_error   - Skips the wrapped method if an error is present in the instance
                    - I am using this to exit out of deep recursions if there is an error
                    - This can only be used on instance methods, e.g self is first parameter in method

    Parameters:
        func                        This parameter is handled by the decorator
        error_attribute             The attribute to search for
        method_has_return           True or False depending on whether the function being wrapped returns a value
        error_return                Value to return if the attribute is not equal to the attribute_default_value
        attribute_default_value     Non-error value for the error_attribute

    """

    if func is None:
        return functools.partial(skip_if_error,
                                 error_attribute=error_attribute,
                                 method_has_return=method_has_return,
                                 error_return_value=error_return_value,
                                 attribute_default_value=attribute_default_value)

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if getattr(self, error_attribute, None) == attribute_default_value:
            output = func(self, *args, **kwargs)
        else:
            output = error_return_value

        if method_has_return:
            return output

    return wrapper
