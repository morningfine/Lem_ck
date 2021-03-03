# 问：如何判断某个对象是不是迭代器
# 答：有两种方法
# 方法一： isinstance(obj,Iterator)
# 方法二： 看对象有没有 __iter__属性和__next__属性
#  迭代器的协议：
#  1.迭代器类型必须实现__iter__和 __next__（Python2中是next)
#  2. __iter__方法必须 返回 self
#  3. __next__必须返回下一个值，如果没有下一个则抛出StopIterator异常
from typing import Iterator  # list  tuple  dict  int

# isinstance 是内置函数

obj = iter(range(1, 2))  # 把range(1,2)转换为Iterator类型
for attr in dir(list):
    print(attr)  # __iter__

for attr in dir(obj):
    print(attr)  # __iter__   ...  __next__
print(isinstance([1, 2], list))  # True
print(isinstance(obj, Iterator))  # True
print(isinstance([1, 2], Iterator))  # False
