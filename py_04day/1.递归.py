"""
遍历目录：请用递归方法输出某文件夹下的所有文件的绝对路径
"""
import os


def print_all_files(file_path):
    for root, dirs, files in os.walk(file_path):
        for filename in files:
            print(os.path.join(root, filename))


def print_all_files2(file_path):
    """
    思路：获得file_path下的所有文件及文件夹    # os.scandir(file_path)  os.listdir(file_path)
    如果是文件，直接输出
    如果是文件夹，递归调用print_all_files2(文件夹)
    """
    for item in os.scandir(file_path):
        if item.is_file():
            print(item.path)  # 输出文件夹下的所有文件
        elif item.is_dir():
            print("~~~~~~")
            print_all_files2(item.path)  # 有多少个文件夹，print_all_files2函数就被调用多少次


def recoder(n):
    print(f"这是第{n}层录屏")
    if n == 1:
        return None  # 结束递归，因为不结束就会无限递归
    else:
        n -= 1  # 每递归一次，把层数-1
        recoder(n)  # 第n层递归


if __name__ == '__main__':
    p = "C:/Users/10795/PycharmProjects/python_advance_programming"
    print_all_files2(p)
    recoder(4)
