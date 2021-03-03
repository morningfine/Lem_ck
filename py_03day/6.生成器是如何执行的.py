def f():
    print("开始执行")
    a = 1
    yield a
    print("~~~~~~~~~~~")
    a = 2
    yield a


def f2():
    result = []
    result.append(1)
    result.append(2)
    return result


# 当要访问生成器的__next__方法时，函数会编程running状态，当执行完yield时，函数变成非running状态（即挂起），
# 只有再次执行生成器对象的__next__方法时函数才会被唤醒。
# 想一想： 什么情况下会执行生成器对象的__next__方法呢？（获取生成器下一个值的时候）
if __name__ == '__main__':
    obj = f()  # 如果一个函数中有yield关键字，调用函数的时候不会执行函数的内容，会返回一个对象（这个对象类型是生成器类）
    for i, value in enumerate(obj):
        print(i, value)
    # print(obj.__next__())
    # print(obj.__next__())
    # print(obj.__next__())
    print(type(obj))
    print(hasattr(obj, "__next__"))
    print(hasattr(obj, "__iter__"))
# yield  return 区别
# 共同点：都是Python的关键字
# 不同点：return 是结束函数并返回值，yield是暂时离开函数
