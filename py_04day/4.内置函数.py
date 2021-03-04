# map
# zip
# reduce

def f(x, y):
    return x + y


print(list(map(f, [10, 20, 30], [1, 2, 3])))
print(list(map(lambda x, y: x + y, [10, 20, 30], [1, 2, 3])))  # map 、匿名函数的应用


def zip_test():
    a = ['a', 'b']
    b = [1, 2]
    print(zip(a, b))  # <zip object at 0x000001AD5168BCC0>
    for item in zip(a, b):
        print(item)


zip_test()
