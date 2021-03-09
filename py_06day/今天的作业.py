"""
1. 总结笔记
    重难点：
    1）.什么是单例模式
    2）. 什么是装饰器，带参数的装饰器的调用过程
    3）__new__和__init__的区别和联系
    4）super是什么
2.实现一个类，前5次创建对象，以后创建返回5个中随机的一个
"""
import time
from types import FunctionType


class CallTime:

    def __init__(self, func: FunctionType):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"函数{self.func.__name__}执行时间为{end-start}.")
        return result


@CallTime
def f(a, b):
    time.sleep(1)
    return a + b


@CallTime
def f1():
    time.sleep(3)


if __name__ == '__main__':
    print(f(1, 2))
    f1()
