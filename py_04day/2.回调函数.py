# 函数： 用一块代码实现某个特定的功能
# 回调函数：（回调模式）如果一个函数的参数是函数类型，那么我们可以把这个参数叫做回调函数
# 下面用代码演示：
# 比较2个数的大小，并用不同风格输出    例如：  compare 1  and 2, min = 1    1和2比较，最小的是1

# 函数中调用函数：1.如果调用的是自身，叫递归；2.如果调用的是别的函数，叫普通调用；3.如果借用参数调用的别的函数，叫回调；
def get_min(a, b, func):  # 来： 传来的函数func； 回：我把参数回传给你——func
    # func是回调函数的引用
    result = a if a < b else b
    func(a, b, result)  # 回调
    f()  # 普通调用


def f():
    pass


# 回调函数一
def call_back_print_en(a, b, _min):
    print(f"compare {a} and {b},min={_min}")


# 回调函数二
def call_back_print_zh(a, b, _min):
    print(f"{a} 和 {b}比较,{_min}最小")


if __name__ == '__main__':
    get_min(1, 2, call_back_print_zh)
