import time

"""
缺少IO检测
"""


def work1():
    for i in range(5):
        print('work1:听音乐...')
        time.sleep(1)
        yield


def work2():
    for i in range(5):
        print('work2:打游戏...')
        time.sleep(1)
        yield


def calc_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'共花费{(end - start):.2f}秒')

    return wrap


@calc_time
def main():
    g1 = work1()
    g2 = work2()
    while True:
        try:
            next(g1)
            next(g2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
