# 预习 装饰器
# 写一个装饰器，用来统计任何函数的运行时间

def cal_time():
    pass


@cal_time
def f():
    print("do something ...")
