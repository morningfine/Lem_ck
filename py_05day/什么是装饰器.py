"""
装饰器设计模式

【生活中】
手机壳
白色手机  + 黑色的手机壳  （白色手机并没有收到实质性的变化）

【工作中装饰器的作用】
1. 用装饰器写的代码优雅
    需求： 无极想自己做一个 类似Flask的框架，Grass 小草
        解决路由问题    http://localhost/hello    hello函数
                    http://localhost/home     home函数
    解决方案：
        1）怎么才能让使用者更方便
2. 在不更改函数的基础上，为函数添加额外的功能
"""


def hello():
    print("hello")


def home():
    print("home")


url_map = {
    "http://localhost/hello": hello,
    "http://localhost/home": home
}

while True:
    url = input("请输入url：")
    if url == "exit":
        break
    try:
        url_map[url]()
    except KeyError as e:
        print(404)
