import logging

log_method = []
def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if (level == "warn"):
                logging.warn(" method : {}".format(func.__name__))
            if (level == "info"):
                logging.info(" method : {}".format(func.__name__))
            if (level == "error"):
                logging.error(" method : {}".format(func.__name__))
            func(*args, **kwargs)
            log_method.append(func.__name__)
        return wrapper
    return decorator
    

@log(level="warn")
@log(level="error")
def foo(arg1, arg2):
    print "foo is run {} {}".format(arg1, arg2)

# foo = log(foo)
foo(arg1 = "ffff", arg2 = "cccc")
print log_method