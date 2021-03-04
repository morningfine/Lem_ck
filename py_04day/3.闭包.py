"""
闭包也是一个函数

需求：检测任意函数的参数
"""
import logging


def f1(a, b):
    print("hello")


def f2(x, y):
    pass


# 用闭包实现
def logger(func):
    def log_func(*args):
        logging.basicConfig(filename="demo.log", level=logging.INFO)
        logging.info(f"{func.__name__} is running, arguments is {args}")

    # 返回 log_func 不加括号  ,这里就是闭包
    return log_func  # 把log_func函数的引用 传给 logger的调用者


f1_logger = logger(f1)  # def f1(a,b):pass
f2_logger = logger(f2)  # def f2(x,y):pass
f1_logger(1, 2)
f2_logger(10, 20)
logger(f1)(1, 2)


def outer_function(n):
    num = n

    def inner_function():
        # nonlocal 一般用在嵌套函数中
        nonlocal num  # global(全局) local(局部)  nonlocal(不在本局部，但不是全局)
        print("hello")
        num -= 1

    # 不加括号，返回inner_function()函数的函数名（即引用）
    return inner_function


# 一般情况，函数结束，函数里面所有的局部变量都会被销毁
# 问： 函数调用结束后，我怎么才能获得函数里面的局部变量？
# 答：使用闭包（ 在函数里面再定义一个函数，把局部变量暴露给外部  ）
my_func = outer_function(3)
my_func()


# 写一个方法，实现 记录某个函数被调用的次数
# 闭包实现：某个函数 当做内层函数，外部的函数加一个c变量用来统计内层函数调用的次数
def outer():
    c = 0  # 用来记录 inner调用的次数

    def some_function():
        nonlocal c
        c += 1
        print(c)

    return some_function


count_some_function = outer()
count_some_function()  # 1
count_some_function()  # 2
count_some_function()  # 3

# Python 面向对象   ： 闭包能实现的，用类也能实现
# C语言 ：  函数式编程，没有类，怎么办？

