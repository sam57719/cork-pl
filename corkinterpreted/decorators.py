import functools


def check_for_instance_error(func=None, attribute: str = 'error', method_has_return: bool = False,
                             error_return: any = None, check_before: bool = True):

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
