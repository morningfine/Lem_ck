# 对齐缩进（相对于函数括号的左边对齐）
def func(name=None, age=None, gender=None,
         name1=None, age1=None):
    pass


# 层级缩进（缩进两个tab键或4个空格）
def func1(
        name=None, age=None, gender=None,
        name1=None, age1=None, gender1=None):
    return 1


# 悬挂缩进
f = func1(
    name=None, age=None, gender=None,
    name1=None, age1=None, gender1=None)

# 单行代码数不要超过79个字符
# 如果超过，使用反斜杠“\”来作为隐式换行
with open(r"D:\project\pythonProject\Lem_ck\py_o1day\test.txt") as f1, \
        open(r"D:\project\pythonProject\Lem_ck\py_o1day\test.txt", "w") as f2:
    content = f1.read()
    f2.write(content)


# Ctrl+Alt+L （根据pep8规范格式化代码）
# 函数间隔或类间隔要空两行
class MyTest:
    pass

