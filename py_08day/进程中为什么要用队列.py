"""
multiprocessing.Queue  :  管道   序列化      进程安全
 了解： MQ （Message Queue）    Redis   rabitMq    kafka
"""
from multiprocessing import Process, Queue


def work01(q: Queue):
    """

    :param q: 要处理的所有任务
    :return: None
    """
    print('work01中的参数q的id：', id(q))
    while not q.empty():
        print(f'work01从q中获得了{q.get()}')


def work02(q: Queue):
    """
    :param q: 要做的所有任务
    :return: None
    """
    print('work02中的参数q的id：', id(q))
    while not q.empty():
        print(f'work02 从q中获得了{q.get()}')


if __name__ == '__main__':
    q = Queue()
    q.put('a')
    q.put('b')
    q.put('c')
    p1 = Process(target=work01, args=(q,))  # 子进程 q1
    p2 = Process(target=work02, args=(q,))  # 子进程 q2
    p1.start()
    p2.start()
    print(f'主进程运行完毕！')
# 使用list： work01 work02会做重复工作   p1 p2 进程 独享 list内存
# 使用Queue： work01 work02共同完成q中的所有任务     Queue 是被 p1 p2 共享的
