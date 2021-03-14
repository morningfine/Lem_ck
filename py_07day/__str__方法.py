print(hasattr(list, '__str__'))  # True
print([1, 2, 3])


class MyList(list):
    def __str__(self):  # print 对象时 对象输出的样子
        result = ''
        for value in self:
            result += str(value)
        return f"list:{result}"


nums = MyList([1, 2, 3])
print(nums)
