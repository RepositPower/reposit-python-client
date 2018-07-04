def add_functions_as_methods(functions):
    def decorator(_class):
        for _function in functions:
            setattr(_class, _function.__name__, _function)
        return _class
    return decorator
