import os


def print_path(path_param):
    for item in os.scandir(path_param):
        if item.is_file():
            print(os.path.abspath(item))
            # print(os.path(item))
        else:
            print_path(item)
            print("hhh")


if __name__ == '__main__':
    path = r"D:\zcg_project\Lem_ck"
    print([item.is_file() for item in os.scandir(path)])
    print_path(path)
