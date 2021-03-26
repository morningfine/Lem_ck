"""
2. （选做）挑战使用多线程或多进程实现下载某个网络资源。（例如：古诗文）

例如：下载4页有关写春天的句子的网页

【操作步骤】

1）把4个页面添加到队列（如果是多进程必须用队列；如果是多线程可以用list，但还是推荐用内置的队列，因为list不是线程安全的）
第1页：https://so.gushiwen.org/mingjus/default.aspx?page=1&tstr=%E6%98%A5%E5%A4%A9
第2页：https://so.gushiwen.org/mingjus/default.aspx?page=2&tstr=%E6%98%A5%E5%A4%A9
第3页：https://so.gushiwen.org/mingjus/default.aspx?page=3&tstr=%E6%98%A5%E5%A4%A9
第4页：https://so.gushiwen.org/mingjus/default.aspx?page=4&tstr=%E6%98%A5%E5%A4%A9

2）定义一个用于保存网页的函数——downloader

    保存可以用requests库先请求地址，然后把返回的信息写到文件中，可以参考网络上的代码。

3) 使用多线程或多进程执行downloader

【预期结果】

把网页保存成 春天1.html  春天2.html 春天3.html  春天4.html
"""
import re
import time
import requests
from threading import Thread
from multiprocessing import Queue, Process


def downloader(q: Queue):
    while not q.empty():
        qid = q.get()
        url = f"https://so.gushiwen.org/mingjus/default.aspx?page={qid}&tstr=%E6%98%A5%E5%A4%A9"
        html_sourc = requests.request("get", url, verify=False).text
        # patterncss = '<link rel="stylesheet" href="(.*?)"'
        # patternjs = '<script src="(.*?)"'
        # patternimg = '<img src="(.*?)"'
        # print(html_sourc)
        # css_list = re.findall(patterncss, html_sourc)
        # print(css_list)
        # for i in css_list:
        #     print(i)
        # with open(f"./asset/css/")
        with open(f"./春天{qid}.html", "wb", encoding="utf-8") as f:
            f.write(html_sourc)
        time.sleep(1)
    # print(text1)


if __name__ == '__main__':
    t1 = time.time()
    q = Queue()
    for i in range(1, 5):
        q.put(i)
    # p = Process(target=downloader, args=(q,))
    p1 = Process(target=downloader, args=(q,))
    p2 = Process(target=downloader, args=(q,))
    p3 = Process(target=downloader, args=(q,))
    p4 = Process(target=downloader, args=(q,))
    # p1 = Thread(target=downloader, args=(q,))
    # p2 = Thread(target=downloader, args=(q,))
    # p3 = Thread(target=downloader, args=(q,))
    # p4 = Thread(target=downloader, args=(q,))
    # p.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p4.join()
    t2 = time.time()
    print("共耗时{}".format(t2-t1))
