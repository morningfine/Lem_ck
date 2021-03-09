# 用类装饰某个函数

class A:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):  # __call__ 当对一个对象加（）进行调用时，此方法会自动执行
        pass


@A
def f(a, b):
    pass


if __name__ == '__main__':
    print(hasattr(f, '__call__'))
    print(hasattr(A, '__call__'))
    f(1, 2)
