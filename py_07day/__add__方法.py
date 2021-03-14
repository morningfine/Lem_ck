"""
对同类型的2个对象进行 + 操作，会执行对象的 __add__方法
"""


class Myclass(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # self： 第一个对象
        # other： 第二个对象
        return "hi"


if __name__ == '__main__':
    obj1 = Myclass(1)
    obj2 = Myclass(2)
    obj3 = object.__new__(Myclass)  # 创建对象
    obj3.__init__(3)  # 初始化对象
    print(obj3.value)
    print(obj1 + obj2)  # Myclass(obj1,obj2)
    print(obj1.__add__(obj2))
