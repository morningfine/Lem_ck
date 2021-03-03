from typing import Iterable


# 问：如何判断一个对象是不是可迭代对象
# 答：有两种方法
# 方法一：isinstance(obj,Iterable)
# 方法二：看有没有__iter__方法

def my_range(stop):
    """模拟了Python2中的range"""
    value = 1
    result = []
    while value < stop:
        result.append(value)
        value += 1
    return result


nums = my_range(5)
for num in nums:
    print(num)

for num in nums:
    print(num)
# Python2 中 有 xrange和 range函数
# Python3 中 只有 range

if __name__ == '__main__':
    print(my_range(10))  # 1 2 3 4 5 6 7 8 9
    print(isinstance(my_range(10), Iterable))
    # print(my_range(999999999999999999999999999999999))
