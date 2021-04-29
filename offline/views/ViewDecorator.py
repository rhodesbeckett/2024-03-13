def widget_decorator(func):
    def wrapper(*args,):
        args[0].method_part()
        func(args[0])
        args[0].frame_part()
    return wrapper