import functools


def check_for_instance_error(func=None, attribute: str = 'error', method_has_return: bool = False,
                             error_return: any = None, check_before: bool = True):
    """
    check_for_instance_error - Checks whether a given instance value is None or not
                             - I am using this to exit out of deep recursions if there is an error

    Parameters:
        func                This parameter is handled by the decorator
        attribute           The attribute to search for
        method_has_return   True or False depending on whether the function being wrapped returns a value
        error_return        Value to return if the attribute is not None
        check_before        True or False depending on whether you want the attribute check to happen after or before
                            the function call

    """

    if func is None:
        return functools.partial(check_for_instance_error,
                                 attribute=attribute,
                                 method_has_return=method_has_return,
                                 error_return=error_return,
                                 check_before=check_before)

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):

        if not check_before:
            output = func(self, *args, **kwargs)
            if getattr(self, attribute, None) is not None:
                output = error_return

        else:
            if getattr(self, attribute, None) is None:
                output = func(self, *args, **kwargs)
            else:
                output = error_return

        if method_has_return:
            return output

    return wrapper
