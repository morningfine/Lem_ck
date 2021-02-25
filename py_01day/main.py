from py_01day.book import BookManage, Book


def welcome():
    """
    欢迎提示语：
    :return:
    """
    print("*******************欢迎进入图书管理系统**********************")
    print("1.显示所有图书\n2.添加图书\n3.删除图书\n4.查找图书\n5.退出\n6.清空数据\n7.保存")
    print("**********************************************************")


def choose_num():
    """
    选择数字
    :return: 返回选择的数字
    """
    num = input("请输入你的选择：")
    # 如果编号不是数字  或者  不是 1，2,3,4,5  返回 -1
    if not num.isdigit() or num not in ["1", "2", "3", "4", "5", "6", "7"]:
        return "-1"
    return num


def main():
    bm = BookManage()  # 创建一个图书管理系统的对象
    while True:
        welcome()  # 欢迎提示语
        choose = choose_num()  # 选择数字
        if choose == "-1":
            print("输入的有误，请重新输入！")
        elif choose == "1":
            bm.show_all_books()
        elif choose == "2":
            num = bm.last_book_id + 1
            name = input("请输入图书名字：")
            position = input("请输入图书位置：")
            book = Book(num, name, position)
            bm.add_book(book)
        elif choose == "3":
            num = input("请输入要删除的图书编号：")
            bm.del_book(num)
        elif choose == "4":
            num = input("请输入要查找的图书编号：")
            bm.find_book(num)
        elif choose == "5":
            break
        elif choose == "6":
            bm.clear()
        elif choose == "7":
            bm.save()
        else:
            break


if __name__ == '__main__':
    main()
