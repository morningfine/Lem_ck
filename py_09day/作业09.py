"""
1、简单描述同步和异步的区别
答： 同步是当前进程返回实际结果后，才开始下一个任务，异步是当前进程没有返回最终结果就开始下一个任务

2、一个列表中有100个url地址（假设请求每个地址需要0.5秒），请设计程序一个程序，获取列表中的url地址，使用4个线程去发送这100个请求，计算出总耗时！
"""
import time
from multiprocessing.pool import ThreadPool
from queue import Queue


def send_request(q: Queue):
    while not q.empty():
        print(q.get())
        time.sleep(0.5)
        q.task_done()


def calc_time(fun):
    def wrap(*args, **kwargs):
        t1 = time.time()
        fun(*args, **kwargs)
        t2 = time.time()
        print(f"共耗时{t2-t1}秒！")
    return wrap


@calc_time
def main():
    q = Queue()
    for i in range(1, 101):
        q.put(f'http://www.gushi.com/page={i}')
    po = ThreadPool(4)
    po.apply_async(send_request, args=(q, ))
    q.join()


if __name__ == '__main__':
    main()

"""
import time
import threading

lock = threading.Lock()

urls = []
for i in range(100):
    url = f"www.baidu{i}.com"
    urls.append(url)


def send_request():
    while 0 < len(urls):
        lock.acquire()
        print(f"send request {urls.pop(0)}")
        lock.release()
        time.sleep(0.5)


if __name__ == '__main__':
    start_time = time.time()
    thr1 = threading.Thread(target=send_request)
    thr2 = threading.Thread(target=send_request)
    thr3 = threading.Thread(target=send_request)
    thr4 = threading.Thread(target=send_request)
    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()
    thr4.join()
    end_time = time.time()
    print(f"主程序执行完成！耗时{(end_time-start_time):.2f}!")

"""
# import time
# from multiprocessing import Pool
#
#
# def send_request(st):
#     print(f"send request {st}")
#     time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     urls = []
#     for i in range(100):
#         url = f"www.baidu{i}.com"
#         urls.append(url)
#
#     po = Pool(4)
#     po.map(send_request, urls)
#     po.close()
#     t2 = time.time()
#
#     print("主程序执行完毕")
#     print(f"共计耗时{(t2-t1):.2f}!")

