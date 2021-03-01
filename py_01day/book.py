import pickle
import os


class Book:
    def __init__(self, num, name, position):
        """
        图书属性
        :param num: 图书编号
        :param name: 图书名字
        :param position: 图书位置
        :return:
        """
        self.num = num
        self.name = name
        self.position = position

    def __str__(self):
        """
        "自定义print对象时显示的格式
        :return:
        """
        return f"{self.num}\t{self.name}\t{self.position}"


class BookManage:
    # 定义一个图书库
    book_lists = []

    def __init__(self):
        """
        构造函数
        """
        print("=====__int__方法正在执行!=========")

        # 避免异常有两种方法：一、加判断；二、异常处理

        # 确保每次运行程序前，先把book.data文件中所有内存load到book_list中
        if os.path.isfile("book.data"):
            self.book_lists = pickle.load(open("book.data", "rb"))  # 将文件数据加载到内存中
            print(self.book_lists)
        else:
            pickle.dump(self.book_lists, open("book.data", "wb"))  # 将内存数据保存在文件中

        # try:
        #     self.book_lists = pickle.load(open("book.data", "rb"))  # 将文件数据加载到内存中
        # except FileNotFoundError as e:
        #     pickle.dump(self.book_lists, open("book.data", "wb"))  # 将内存数据保存在文件中
        #     print("文件创建成功！")

    def show_all_books(self):
        """
        展示所有的图书
        :return:
        """
        for book in self.book_lists:
            print(book)

    def add_book(self, book: Book):
        """
        添加图书
        :return:
        """
        self.book_lists.append(book)

    def del_book_by_id(self, num):
        """
        删除图书
        :return:
        """
        num = int(num)
        for book in self.book_lists:
            if num == book.num:
                self.book_lists.remove(book)
                print("删除图书成功！")
                break
        else:
            print("图书编号{}不存在".format(num))

    def find_book(self, num):
        """
        查看图书信息
        :param num:
        :return:
        """
        num = int(num)
        for book in self.book_lists:
            if num == book.num:
                print(book)
                print("查找图书成功！")
                break
        else:
            print("图书编号{}不存在".format(num))

    def clear(self):
        """
        清空数据
        :return:
        """
        self.book_lists.clear()
        # self.book_lists = []
        print("数据已清空！")

    def save(self):
        """
        保存数据
        :return:
        """
        pickle.dump(self.book_lists, open("book.data", "wb"))
        print("图书保存成功！")

    @property
    def last_book_id(self):
        """
        如果book_list是空，返回0，否则,返回最后一本书的num值
        :return:
        """
        if self.book_lists:
            book = self.book_lists[-1]  # 获取列表最后一本书
            return book.num
        return 0

    def __del__(self):
        """
        析构函数
        :return:
        """
        print("__del__ is running ....")
        print(self.book_lists)
        pickle.dump(self.book_lists, open("book.data", "wb"))
