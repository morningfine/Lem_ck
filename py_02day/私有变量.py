def test_private_vs_protected_vs_public():
    # public： 共有的
    # protected: 受保护的。  不能被其他文件导入
    # private: “私有的”   你的牙刷
    pass

x = 2
_y = 10  # protected


class A(object):
    def __init__(self):
        self.__z = 2  # 私有属性

    def __some_method(self):  # 私有方法
        print(self)


a = A()

if __name__ == '__main__':
    test_private_vs_protected_vs_public()
