"""
with
上下文管理协议 ： 对象一定包含  __enter__()  和  __exit__() 方法
被with包裹的代码块在执行前先执行__enter__方法，代码块执行结束后会执行__exit__方法
"""


class MyClass(object):

    def __enter__(self):
        print("enter .....")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit.....')


# open方法返回一个对象——文件对象，文件对象支持上下文管理协议
f = open("temp.txt", 'w')
print(hasattr(f, '__enter__'))  # True
print(hasattr(f, '__exit__'))  # True
f.close()

with open("temp.txt", 'w') as f:
    pass

obj = MyClass()
with obj as o:
    print("~~~~~~~~~~")
