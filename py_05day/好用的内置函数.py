# filter(怎么过滤,要过滤的对象) 过滤  从可迭代对象中筛选出满足条件的元素
# map(如何映射，[要映射的对象1,要映射的对象2....]
# reduce  ((((1+2)+3)+4)+5)
from functools import reduce


def reduce_test():
    # 累加功能： 1~5做累加  [1,2,3,4,5]  = > (((1+2) + 3) + 4)
    def f(x, y):
        result = x + y
        return result

    print(sum([1, 2, 3, 4, 5]))
    print(reduce(f, [1, 2, 3, 4, 5]))


def map_test():
    # map(func, *iterables) --> map object  (map对象是一个迭代器)
    #     Make an iterator that computes the function using arguments from
    #  [1,2,3,4]  [10,20,30,40]    =>  [11,21,31,41]

    nums1 = [1, 2, 3]
    nums2 = [10, 20, 30, 40]
    nums3 = [1, 1, 1]
    result = []
    for i, value1 in enumerate(nums1):
        result.append(value1 + nums2[i])

    def f(x, y, z):
        return x + y + z

    print("使用map实现：", list(map(f, nums1, nums2, nums3)))
    print("使用map实现：", list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3)))
    return result
    # return map()  # 把两个列表中每个元素相加，生成新的列表
    # return map(lambda x: (2 * x + 2), [1, 2, 3])  # 对 [1,2,3]中的每一个元素 做 2*x +2 的处理


def filter_test():
    # def f(x):
    #     if x > 2:
    #         return True
    #     return False

    return filter(lambda x: x > 2, [1, 2, 3])
    # return filter(f, [1, 2, 3])  # 对[1,2,3]中的所有元素依次进行f操作
    # return filter(None, [1, 2, 3])  # None 代表：对[1,2,3]不做任何操作


def zip_test():
    """
     zip(*iterables) --> A zip object yielding tuples until an input is exhausted.

       >>> list(zip('abcdefg', range(3), range(4)))
       [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    """
    print(list(zip('abcdefg', range(3), range(4))))



if __name__ == '__main__':
    # for value in filter_test():
    #     print(value)
    # for value in map_test():
    #     print(value)
    reduce_test()
