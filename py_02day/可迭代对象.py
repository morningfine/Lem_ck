# 可迭代对象，可以用for操作的对象都是可迭代对象
# list  tuple  str   set  dict
for i in [1, 2, 3]:
    print(i)
print(hasattr(list, "__iter__"))
print(hasattr(tuple, "__iter__"))
print(hasattr(str, "__iter__"))
print(hasattr(set, "__iter__"))
print(hasattr(dict, "__iter__"))
print(hasattr(int, "__iter__"))  # False
for i in 1:  # TypeError: 'int' object is not iterable
    print(i)
