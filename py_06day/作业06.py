"""
实现一个类，前5次创建对象，以后创建返回5个中随机的一个
"""
import random


class Work:
    times = 0
    obj = None
    obj_set = []

    def __init__(self):
        """
        :return:
        """
        pass

    def __new__(cls, *args, **kwargs):
        """
        如果创建次数小于5，则创建对象，否则，从已创建对象中随机选择一个对象返回
        :param args:
        :param kwargs:
        """
        if cls.times < 5:
            cls.obj = super().__new__(cls)
            cls.times += 1
            cls.obj_set.append(cls.obj)
        else:
            cls.obj = cls.obj_set[random.randint(0, 4)]
        return cls.obj


if __name__ == '__main__':
    for i in range(20):
        a = Work()
        print(id(a))
