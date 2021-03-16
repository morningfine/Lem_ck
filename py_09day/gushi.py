from multiprocessing.pool import ThreadPool
import queue


def download(q: queue.Queue):
    while not q.empty():
        print(q.get())
        q.task_done()  # 这个任务做完了


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(1, 5):
        q.put(f'https://so.gushiwen.org/mingjus/default.aspx?page={i}&tstr=%E6%98%A5%E5%A4%A9')

    pool = ThreadPool(2)  # 2个线程
    pool.apply_async(download, args=(q,))  # pool中的多个线程异步地调用指定函数  这里是  download

    q.join()  # 等待所有的任务做完
    print('finished!')
