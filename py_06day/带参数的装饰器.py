"""
用来记录日志的装饰器。
@log(filename='info.log')
def add(a,b):
    ...
@log(filename='xxx.log')
def modify(item):
    ...
"""

print('======')


def log(filename: str):
    def inner(func):
        print(f'{func.__name__}')

        def wrapper(*args, **kwargs):
            print(args)
            func(*args, **kwargs)

        return wrapper

    return inner


@log(filename="xxx.log")
def add(a, b):
    return a + b


add(1, 2)
