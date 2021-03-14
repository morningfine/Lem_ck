from multiprocessing import Process
import os
import time


def work1():
    print(f"子进程1的id为：{os.getpid()}")
    for i in range(5):
        print("work1 is starting!")
        time.sleep(1)


def work2():
    print(f"子进程2的id为：{os.getpid()}")
    for i in range(5):
        print("work2 is starting!")
        time.sleep(1)


if __name__ == '__main__':
    print("main is running!")
    print(f"主进程id：{os.getpid()}")
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    p1.daemon = True
    p2.daemon = True
    p1.start()
    # p1.join()
    p2.start()
    p2.join()

    print("main is over!")
