import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        # 记录函数运行前的时间 start
        start = time.time()
        # 执行函数
        func(*args, **kwargs)
        # 记录函数运行后的时间 end
        end = time.time()
        # 输出函数的运行时间 end - start
        print(f'{func.__name__}运行了{end - start}时间')

    return wrapper


@calc_time  # f 会传给calc_time
def f(a, b):
    time.sleep(1)


if __name__ == '__main__':
    f(1, 2)
