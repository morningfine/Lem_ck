"""
单例模式： 只有一个实例
实现方法：
    方法一：import
    方法二：单例模式
    方法三：装饰器
"""


class Person(object):
    obj = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        """如果对象已经创建，就直接把创建好的对象返回
        如果对象没有创建，就创建对象，并返回"""
        if cls.obj is None:
            cls.obj = super().__new__(cls)  # 分配内存
        return cls.obj


if __name__ == '__main__':
    xiaoming = Person()
    xiaohong = Person()
    print(xiaoming is xiaohong)  # False
    print(id(xiaoming), id(xiaohong))
