import time
from multiprocessing.pool import ThreadPool
from queue import Queue
import asyncio


async def send_request(q: Queue):
    while not q.empty():
        print(q.get())
        await asyncio.sleep(0.5)
        q.task_done()


def calc_time(fun):
    def wrap(*args, **kwargs):
        t1 = time.time()
        fun(*args, **kwargs)
        t2 = time.time()
        print(f"共耗时{t2 - t1}秒！")

    return wrap


async def main():
    q = Queue()
    for i in range(1, 101):
        q.put(f'http://www.gushi.com/page={i}')
    #po = ThreadPool(4)
    #po.apply_async(send_request, args=(q,))
    task1 = asyncio.create_task(send_request(q))
    task2 = asyncio.create_task(send_request(q))
    task3 = asyncio.create_task(send_request(q))
    task4 = asyncio.create_task(send_request(q))
    await task1
    await task2
    await task3
    await task4


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'共花费时间{(end - start):.2f}秒')
