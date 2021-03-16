"""
1、简单描述同步和异步的区别
答： 同步是当前进程返回实际结果后，才开始下一个任务，异步是当前进程没有返回最终结果就开始下一个任务

2、一个列表中有100个url地址（假设请求每个地址需要0.5秒），请设计程序一个程序，获取列表中的url地址，使用4个线程去发送这100个请求，计算出总耗时！
"""
import time
from multiprocessing import Pool
import requests


def send_request(st):
    print(f"send request {st}")
    time.sleep(0.5)


if __name__ == '__main__':
    t1 = time.time()
    urls = []
    for i in range(100):
        url = f"www.baidu{i}.com"
        urls.append(url)

    po = Pool(4)
    po.map(send_request, urls)
    po.close()
    t2 = time.time()

    print("主程序执行完毕")
    print(f"共计耗时{(t2-t1):.2f}!")

