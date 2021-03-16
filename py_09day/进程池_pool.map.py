import time
from multiprocessing import Pool


def square(x):
    print("~~~~~~~~")
    result = x * x
    return result


if __name__ == '__main__':
    start = time.time()
    pool = Pool(2)
    result = pool.map(square, [1, 2, 3, 4, 5, 6, 7, 8])  # map 会阻塞主程序
    print(result)
    pool.close()
    end = time.time()
    print(f'总共用了{(end - start):.2f}')
