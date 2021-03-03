# 手动实现 平方，  传参（1,3)   返回：1  4  9
result = []
for i in [1, 2, 3]:
    result.append(i * i)
print(result)


class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


def squares(start, stop):  # 第二种
    for i in range(start, stop + 1):
        yield i * i


squares2 = (i * i for i in range(1, 4))  # 第三种

print(type(squares(1, 4)))  # <class 'generator'>
print(type(squares2))  # <class 'generator'>
if __name__ == '__main__':
    # iterator = Squares(1, 3)
    iterator = squares(1, 3)
    for i, value in enumerate(iterator):
        print(i, value)
