"""
第1页：https://so.gushiwen.org/mingjus/default.aspx?page=1&tstr=%E6%98%A5%E5%A4%A9
第2页：https://so.gushiwen.org/mingjus/default.aspx?page=2&tstr=%E6%98%A5%E5%A4%A9
第3页：https://so.gushiwen.org/mingjus/default.aspx?page=3&tstr=%E6%98%A5%E5%A4%A9
第4页：https://so.gushiwen.org/mingjus/default.aspx?page=4&tstr=%E6%98%A5%E5%A4%A9
"""
import queue
import threading
import requests
import re


def downloader(q: queue.Queue):
    while not q.empty():
        url = q.get()
        print(url)
        r = requests.get(url)
        page_num = re.findall(r'page=(\d)&tstr', url)[0]
        filename = f'春天{page_num}.html'
        with open(filename, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(1, 5):
        q.put(f'https://so.gushiwen.org/mingjus/default.aspx?page={i}&tstr=%E6%98%A5%E5%A4%A9')

    thread_pool = []
    for i in range(4):
        t = threading.Thread(target=downloader, args=(q,))
        thread_pool.append(t)
        t.start()
    for t in thread_pool:
        t.join()
    print('finished!')
