"""
1、简单描述同步和异步的区别
2、一个列表中有100个url地址（假设请求每个地址需要0.5秒），请设计程序一个程序，获取列表中的url地址，使用4个线程去发送这100个请求，计算出总耗时！
"""
import time
from multiprocessing.pool import ThreadPool
import queue


def download(q: queue.Queue):
    while not q.empty():
        print(q.get())
        time.sleep(0.5)
        q.task_done()  # 这个任务做完了


def calc_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"共花费时间{(end - start):.2f}秒")

    return wrap


@calc_time
def main():
    q = queue.Queue()
    for i in range(100):
        q.put(f'http://www.gushi.com/page={i}')

    pool = ThreadPool(4)  # 4个线程
    pool.apply_async(download, args=(q,))  # pool中的多个线程异步地调用指定函数  这里是  download

    q.join()  # 等待所有的任务做完
    print('finished!')


if __name__ == '__main__':
    main()
