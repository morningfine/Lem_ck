"""
单任务：单任务的应用程序 (cmd.exe),没办法同时执行多条命令
多任务：多任务的应用  windows操作系统， 迅雷 （同时下载多个文件，边下边播）
多任务的实现方式：多进程、多线程、协程
串行运行：在Linux中串行执行多条命令用 &  ， apt install python & apt install mysql
并行运行：在Linux中并行执行多条命令用 &&   apt install python && apt install mysql
并发：迅雷下载同时下载5个电影（单核CPU)
    1个收银员  “同时”  操作5台  收款机    ——  并发
并行：3台电脑分别安装一个MySQL8.0,然后组成MySQL集群，3个MySQL是同时运行（并行）
    5个收银员  同时 操作 5台  收款机   —— 并行

进程： 静态的（软件、程序、代码、函数...)   动态（软件运行、程序运行、代码运行、函数运行），  进程是动态的
    程序是怎么运行的？  操作系统 创建一个进程（加载代码到内存，为变量分配内存，建个档案，process id  PID
"""
from multiprocessing import Process, Queue
import requests
import os

"""
需求：使用多进程实现并发下载图片。
- 多进程会独享资源， 2个进程不能共享变量（例如：不能共享list)  ,如何实现共享资源呢？（队列Queue，内存数据库redis....）
- 多线程占用的资源少，2个线程是共享变量的，迅雷就是使用多线程下载技术。
"""


def download(q: Queue):
    while True:
        url = q.get()
        r = requests.get(url)  # 就像浏览器发请求一样
        img_name = url.split('/')[-1]
        with open(img_name, 'wb') as f:
            f.write(r.content)  # 把服务器返回的信息（图片）保存到文件中
        if q.empty():
            break


if __name__ == '__main__':
    tasks = Queue()
    # put相当于list中的 append方法
    tasks.put("https://www.ketangpai.com/images/common/logo_blue.png")
    tasks.put("https://photo-static-api.fotomore.com/creative/vcg/176/new/862018abb4f74bd0b4f9ad53a3c1250e.jpg")

    p1 = Process(target=download, args=(tasks,))  # 创建一个用来执行download函数的进程p1
    p2 = Process(target=download, args=(tasks,))  # 创建一个用来执行download函数的进程p2
    p1.start()  # 启动进程p1
    p2.start()  # 启动进程p2
    # 进程启动后，是由操作系统控制执行的
