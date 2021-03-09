"""
@A
def f(a,b):
    pass
f 传给 A
"""
import time


class CalTime(object):
    def __init__(self, func):  # 返回一个对象：__init__方法首先会初始化对象，并把对象返回。
        self.func = func
        print("~~~~~~")

    def __call__(self, *args, **kwargs):  # __call__当对一个对象加()进行调用的时候，此方法会自动执行
        print(f"{self.func.__name__}函数运行前")
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__}函数运行后")
        end = time.time()
        self.log()
        print(f'{self.func.__name__}的运行时间为{end - start}')
        return result

    def log(self):
        pass


@CalTime  # 类，f会传给类，然会返回一个A的实例
def f(x, y):
    time.sleep(1)
    print(x)
    pass
    return x + y


if __name__ == '__main__':
    print(f(1, 2))

    # a = A(f)
    # 类，函数 直接加括号时可以的，
    # 由类创建的对象，一般时不能加括号的
    # a(1, 2)  # TypeError: 'A' object is not callable

    # print(type(f))
    # print(type(a))
    # print(hasattr(f, '__call__'))
    # print(hasattr(A, '__call__'))

# nums = [1, 2]
# print(nums, hasattr(nums, '__call__'))
#
#
# class MyList(list):
#     def __call__(self, *args, **kwargs):
#         pass
#
#
# my_nums = MyList("123")
# my_nums()
# print(my_nums)
