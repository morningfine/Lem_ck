#  需求： 为 字符串 添加修饰 。 hello  = > <i>hello</i>   hello =>  <b>hello</b>
from types import FunctionType


def add_itali(s):
    return "<i>" + s + "</i>"


def add_bold(s):
    return "<b>" + s + "</b>"


if __name__ == '__main__':
    print(add_itali("hello"))
    print(add_bold("hello"))
    print(type(add_itali))
