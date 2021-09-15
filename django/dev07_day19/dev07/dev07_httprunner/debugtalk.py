
import time
import random


def sleep(n_secs):
    time.sleep(n_secs)


def random_generate_uagent():
    user_agent_list = ["Mozilla/5.0", "Mozilla/5.0 buyu", "Mozilla/5.0 duohe", "Mozilla/5.0 lemon", "Mozilla/5.0 xxx"]
    return random.choice(user_agent_list)


def get_accounts():
    accounts = [
        {"title": "正常登录", "username": "keyou1", "password": "123456",
            "status_code": 200, "msg": "token"},
        {"title": "密码错误", "username": "keyou1", "password": "123457",
            "status_code": 400, "msg": "non_field_errors"},
        {"title": "账号错误", "username": "keyou1111", "password": "123456",
            "status_code": 400, "msg": "non_field_errors"},
        {"title": "用户名为空", "username": "", "password": "123456",
            "status_code": 400, "msg": "username"},
        {"title": "密码为空", "username": "keyou1", "password": "",
            "status_code": 400, "msg": "password"},
    ]
    return accounts


if __name__ == '__main__':
    print(random_generate_uagent())
