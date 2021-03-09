def add(x, y):
    return x + y


class MyClass(object):
    pass


class MyClass2(object):
    def __call__(self, *args, **kwargs):
        pass


print(callable(add))  # True
print(callable(MyClass()))  # False
print(callable(MyClass2()))  # True
