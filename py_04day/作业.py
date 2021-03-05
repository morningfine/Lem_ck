"""

nums = [1,22,33,4,7,-1]   ==>  [22,33,7]
把大于5的数过滤出来，放到一个新列表中
"""
# 使用尽可能好的方法，从多个整数组成的列表中过滤出大于5的数。（可以试着多写几种方法）
"""
nums = [1,22,33,4,7,-1]   ==>  [22,33,7]
把大于5的数过滤出来，放到一个新列表中
"""


def filter1(li: list):
    li1 = []
    for i in li:
        if i > 5:
            li1.append(i)
    return li1


def filter2(li: list):
    return [i for i in li if i > 5]


def filter3(li: list):
    for i in li:
        if i <= 5:
            li.remove(i)
    return li


if __name__ == '__main__':
    nums = [1, 22, 33, 4, 7, -1]
    print(filter1(nums))
    print(filter2(nums))
    print(filter3(nums))
