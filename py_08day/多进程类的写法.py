from multiprocessing import Process


class MyProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        print("hello ")


if __name__ == '__main__':
    p1 = MyProcess()
    p2 = MyProcess()
    p1.start()  # 会调用 MyProcess中的run方法
    p2.start()
