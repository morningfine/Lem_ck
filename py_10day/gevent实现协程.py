import time
from gevent import monkey

monkey.patch_all()
import gevent


def work1():
    for i in range(5):
        print('work1:听音乐...')
        time.sleep(1)


def work2():
    for i in range(5):
        print('work2:打游戏...')
        time.sleep(1)


def main():
    g1 = gevent.spawn(work1)  # 创建协程1
    g2 = gevent.spawn(work2)  # 创建协程2
    g1.join()
    g2.join()
    print('所有任务执行完毕！')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'总共花费{(end - start):.2f}秒。')

