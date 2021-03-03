#  迭代器的协议：
#  1.迭代器类型必须实现__iter__和 __next__（Python2中是next)
#  2. __iter__方法必须 返回 self
#  3. __next__必须返回下一个值，如果没有下一个则抛出StopIteration异常
#  4. 对迭代器进行for操作时，每次操作都会执行__next__方法
#  5. 只能迭代一遍。
#  6. for语句的迭代，会忽略StopIteration异常
#  7. 迭代器 与 list相比，迭代器省内存

# range(1,5)  1,2,3,4
# Next(5)  1 2  3 4
class Next(object):
    def __init__(self, stop, start=0):
        self.start = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        """如果有下一个数，则返回下一个数；如果没有下一个数，则抛出StopIteration异常"""
        if self.start >= self.stop - 1:
            raise StopIteration
        self.start += 1
        return self.start


if __name__ == '__main__':
    obj = Next(5)
    for i, value in enumerate(obj):
        print(i, value)
    for i in obj:
        print(i)
    print(obj.__next__())  # 异常
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    # print(obj.__next__())  #
