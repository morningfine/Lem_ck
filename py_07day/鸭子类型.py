class Cat(object):
    def say(self):
        print('miao ... miao')


class Dog(object):
    def say(self):
        print('wangwang ~~~~~')


def f(obj):
    """obj 只要是用say方法的对象就行"""
    obj.say()


if __name__ == '__main__':
    f(Cat())
    f(Dog())

"""
应用场景：发送消息
class Text(object): 
    def send(self):pass
class Image(object):
    def send(self):pass
def send_msg(obj):
    ....
    obj.send()
    .,..

send_msg(Text())
send_msg(Image())
"""
