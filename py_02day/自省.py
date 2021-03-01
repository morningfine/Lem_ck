# 自省： 汉语解释为”自我反省“
# Python的自省：Python运行的时候知道对象自身有哪些东西
class Person(object):
    name = "人"


print(dir(Person))  # dir是自省的一种，作用查看自己有哪些属性
print(hasattr(Person, "name"))  # hasattr是自省的一种，作用查看对象有没有某个属性


# 使用场景举例：  “检查函数参数（类型检查isinstance等）”
def f(i):
    if not isinstance(i, int):
        print(f'{i}不是整数')
    else:
        print(f'{i}是整数')


if __name__ == '__main__':
    f(1)
    f(3.1)

"""
dir()  # Python查看对象有哪些属性
hasattr()  # Python查看对象是否有每个属性
type()     # Python查看对象是什么类型
isinstance()  # Python查看对象是不是某个类型
id()  # Python查看对象的id是什么
callable()  # Python判断对象是不是可调用的（即是不是可以加括号调用）
help()  # Python查看某个对象的帮助信息
getattr()  # 获得某个对象的属性
setattr()   # 设置某个对象的属性
"""
print(type(1))
