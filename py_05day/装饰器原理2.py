#  需求： 为 字符串 添加修饰 。 hello  = > <i>hello</i>   hello =>  <b>hello</b>
from types import FunctionType


def add_itali(func: FunctionType):
    """接收一个函数，返回一个经过装饰的新函数"""

    def new_func():
        return "<i>" + func() + "</i>"

    return new_func


def add_bold(func):
    def new_func():
        s = func()
        result = "<b>" + s + "</b>"
        return result

        # 返回函数名  不要加（）

    return new_func


@add_bold  # 语法糖
def text():
    return "hello"


if __name__ == '__main__':
    # new_function = add_bold(text)
    # new_text = new_function()
    # print(new_text)
    print(text())
