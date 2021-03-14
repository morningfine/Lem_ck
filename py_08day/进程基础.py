import os
import time
from multiprocessing import Process


def play_music():
    print("子进程p1：", os.getpid())
    for i in range(5):
        print('play music ...')
        time.sleep(1)


def play_lol():
    print("子进程p2：", os.getpid())
    for i in range(5):
        print('play lol ...')
        time.sleep(1)


if __name__ == '__main__':
    print('主进程：', os.getpid())
    start_time = time.time()
    p1 = Process(target=play_music)
    p2 = Process(target=play_lol)
    # p1.daemon = True  # 默认值是False，当为True的时候，主进程结束，会强制结束子进程
    # p2.daemon = True
    p1.start()  # 操作系统  启动一个进程  用来运行target=play_music 的 进程，子进程  （不是完整的代码）
    # p1.join()  # 上面的代码任务没有执行完，不会运行下面的代码
    p2.start()
    print(help(p2))
    # p1.join()
    # p2.join()

    # p1 p2 都结束后再 计算时间
    # while True:
    #     if p1.is_alive() or p2.is_alive():
    #         time.sleep(1)
    #     else:
    #         break
    end_time = time.time()
    print(end_time - start_time)

    # 怎么才能保证让主进程最后再结束呢？   用join
    # 主进程： 进程基础.py (代码）       python.exe  进程基础.py  运行的时候， 操作系统会 分一个进程， 这个进程我们称为主进程
    # p1.daemon
    # is_alive()