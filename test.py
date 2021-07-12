import time
import random
import json
# 1625034621779
# 16249531341197307

def get_time_stamp():
    ct = time.time()
    ct = 1625039798.303

    print(ct,type(ct))
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H-%M-%S", local_time)
    print(data_head)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s-%03d" % (data_head, data_secs)
    return time_stamp


num = get_time_stamp()
num1 = random.randint(0, 1)

if __name__ == '__main__':
    json_info = '{"age": "12"}'
    dict1 = json.loads(json_info)
    print(dict1,type(b))
    # print(num1)
    # print(4.15+3.15)
    # print(int(False))

