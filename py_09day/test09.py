import time
from multiprocessing import Pool, Lock, Manager


def send_request(st):
    # lo.acquire()
    print(f"send request {st}")
    time.sleep(0.5)
    # lo.release()


if __name__ == '__main__':
    t1 = time.time()
    urls = []
    # lock = Lock()  # 进程锁
    manager = Manager()
    lock = manager.Lock()
    for i in range(10):
        url = f"www.baidu{i}.com"
        urls.append(lock, url)
    print(urls)

    po = Pool(4)
    po.map(send_request, urls)
    po.close()
    t2 = time.time()

    print("主程序执行完毕")
    print(f"共计耗时{(t2-t1):.2f}!")