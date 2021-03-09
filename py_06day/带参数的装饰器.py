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


class Log1:
    def __init__(self, filename: str):
        self.filename = filename

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(args)
            print(self.filename)
            results = func(*args, **kwargs)
            return results
        return wrapper


@Log1(filename="xxx.log")
def add1(a, b):
    return a + b


if __name__ == '__main__':
    # add(1, 2)
    print(add1(1, 3))
