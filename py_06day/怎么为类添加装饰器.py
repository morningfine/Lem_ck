"""
@some_func
class A(object):
    ...
    pass

A传给some_func
"""


def some_func(cls):
    return cls


@some_func
class A(object):
    pass


if __name__ == '__main__':
    a = A()
