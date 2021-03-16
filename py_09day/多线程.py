import threading
import time


def music(user):
    print(f'{user}正在听音乐....')
    print(f'{threading.current_thread().name}正在运行...')
    time.sleep(5)
    print(f'{threading.current_thread().name}运行即将结束。')


def lol(user):
    time.sleep(8)


if __name__ == '__main__':
    t1 = threading.Thread(target=music, args=('无极',), name='线程1')
    t2 = threading.Thread(target=lol, args=('无极',), name='线程2')
    t1.start()
    t2.start()
    # t1.join()  # 阻塞主程序，但不会阻塞线程2
    # t2.join()
    print('主程序结束！')
