import time
import random


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H-%M-%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s-%03d" % (data_head, data_secs)
    return time_stamp


num = get_time_stamp()
num1 = random.randint(0, 1)

if __name__ == '__main__':
    print(num1)
    print(4.15+3.15)
    print(int(False))

