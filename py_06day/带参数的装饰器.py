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
    print("执行Log1类")

    def __init__(self, filename: str):
        self.filename = filename
        print("执行__init__函数")

    def __call__(self, func):
        print("执行__call__函数")

        def wrapper(*args, **kwargs):
            print("执行wrapper函数")
            print(args)
            print(self.filename)
            results = func(*args, **kwargs)
            return results
        return wrapper


@Log1(filename="xxx.log")
def add1(a, b):
    print("执行add1函数")
    return a + b


if __name__ == '__main__':
    # add(1, 2)
    print(add1(1, 3))
