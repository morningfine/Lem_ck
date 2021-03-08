"""
nums = [1,22,33,4,7,-1]   ==>  [22,33,7]
把大于5的数过滤出来，放到一个新列表中
"""


def filter_nums1(nums, mark=5):
    """
    从nums中过滤出比mark大的数
    :param nums:有数字组成的可迭代对象
    :param mark:过滤的比对标准，默认是5
    :return:返回新的列表
    """
    return [num for num in nums if num > mark]


def filter_nums2(nums, mark=5):
    """
    从nums中过滤出比mark大的数
    :param nums:有数字组成的可迭代对象
    :param mark:过滤的比对标准，默认是5
    :return:
    """
    return list(filter(lambda x: x > 5, nums))


if __name__ == '__main__':
    print(filter_nums2([1, 2, 3, 4, 5, 6, 7, 8]))
