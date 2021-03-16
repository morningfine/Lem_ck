import threading

n = 200000
lock = threading.Lock()
print(hasattr(lock, '__enter__'))  # True
print(hasattr(lock, '__exit__'))  # True


def work():
    global n
    for i in range(1000000):
        # # 上锁
        # lock.acquire()
        # n -= 1
        # # 释放锁
        # lock.release()
        with lock:
            n -= 1


if __name__ == '__main__':
    # 两个线程共同操作n
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(n)
