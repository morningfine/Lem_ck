from book import BookManage


def welcome():
    """
    欢迎提示语：
    :return:
    """
    print("=====欢迎来到图书管理系统======")
    print("请选择你要做的操作：\n1、显示所有图书\n2、添加图书\n3、删除\n4、退出")
    print("=====欢迎来到图书管理系统======")


def main():
    # 创建一个对象
    bm = BookManage()
    welcome()
    while True:
        choose = input("请输入你的选择：")
        if choose == "1":
            show_all_books()



if __name__ == '__main__':
    main()