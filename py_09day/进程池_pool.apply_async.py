import time
from multiprocessing import Pool

"""
apply :  调用函数，传递任意参数
map: 把一个可迭代对象 映射 到 函数
"""


def test(x, y, z=0):  # z=0
    """执行脚本，执行过程需要30分钟"""
    print('~~~~')
    time.sleep(2)
    return x + y


if __name__ == '__main__':
    pool = Pool(2)
    #  apply(self, func, args=(), kwds={})
    #  apply(self,func,*args,**kwds)
    result = pool.apply(test, (2, 3), {'z': 1})  # 阻塞 主程序（主进程）  同步
    pool.apply_async(test, (2, 3))  # 不阻塞 主程       异步
    print("finished!")
