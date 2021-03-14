"""
1. 总结笔记
    重难点：
    1）.什么是单例模式
    2）. 什么是装饰器，带参数的装饰器的调用过程
    3）__new__和__init__的区别和联系
    4）super是什么
2.实现一个类，前5次创建对象，以后创建返回5个中随机的一个
"""
import random


class MyClass(object):
    objs = []  # 已经创建的对象的个数

    def __new__(cls, *args, **kwargs):
        if len(cls.objs) < 5:
            obj = super().__new__(cls)  # 由 MyClass创建一个对象
            cls.objs.append(obj)
        else:
            obj = random.choice(cls.objs)
        return obj


class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        print(f'{self.firstname} {self.lastname}')


class Student(Person):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        # 初始化父类 的方法

        # Person.__init__(self, firstname, lastname)  方法一
        super(Student, self).__init__(firstname, lastname)  # 方法二：Python2 Python3
        super().__init__(firstname, lastname)  # 方法三： Python3

    def show_student(self):
        Person.fullname(self)
        print('Grade', self.grade)


if __name__ == '__main__':
    stu = Student('Tom', 'Then', '测开7期')
    stu.show_student()


class A(object):
    def __init__(self):
        super().__init__()
        print("A....")


class B(object):
    def __init__(self):
        super(B, self).__init__()
        print("B....")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C....")


c = C()
