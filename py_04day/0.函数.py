# 函数也是对象，一切都是对象,任何对象都可以当做参数传给某个函数
# Python中的传参，其实就是把某个对象的引用赋值给变量   （传参就是赋值）
# f()这个函数，f是 function类创建的对象，  [1,2,3] 是 list类创建的对象， dir(f)  id(f)  type(f)


def f():
    pass


def add(x, y):
    """ 两个数相加，返回两个数的和"""
    return x + y


print(type(f))  # <class 'function'>
print(id(f))
print(add(1, 2))
