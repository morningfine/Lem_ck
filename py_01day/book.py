import pickle


class BookManage(object):

    def __init__(self):
        """
        构造函数
        """
        print("=====__int__方法正在执行!=========")

        book_lists = pickle.load(open("book.data"), "rb")

    def __del__(self):
        """
        析构函数
        :return:
        """
        pickle.dump()