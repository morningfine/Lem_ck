# 预习 装饰器
# 写一个装饰器，用来统计任何函数的运行时间

# def cal_time():
#     pass
#
#
# @cal_time
# def f():
#     print("do something ...")

import time
from types import FunctionType


def cal_time(fun: FunctionType):
    def fun1():
        t1 = time.time()
        print(t1)
        fun()
        t2 = time.time()
        print(t2)
        print("函数{}执行的时间为：{}".format(fun.__name__, t2 - t1))
        return t2 - t1
    return fun1


@cal_time
def f():
    print("do something ...")
    sum1 = 0
    for i in range(100000):
        sum1 += i
    print(sum1)


@cal_time
def f1():
    print("do something ...")
    sum1 = 0
    for i in range(100000):
        sum1 += i
    print(sum1)


if __name__ == '__main__':
    print(f())
    print(f1())

