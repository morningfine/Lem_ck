import time
from multiprocessing import Pool


def square(x):
    result = x * x
    print("~~~~~~~~~")
    return result


if __name__ == '__main__':
    start = time.time()
    pool = Pool(2)
    result = pool.map_async(square, [1, 2, 3, 4, 5, 6, 7, 8])  # map 会阻塞主程序
    print(result.get())  # get() 用例 获得map映射后的结果集  [1, 4, 9, 16, 25, 36, 49, 64]  ， 结果不出来，不往下运行 （即阻塞）
    pool.close()
    end = time.time()
    print(f'总共用了{(end - start):.2f}')
