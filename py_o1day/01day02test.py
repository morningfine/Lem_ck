# # 需求1：如何快速生成一个["data01","data1",...."data99"]的列表
# # 列表推导式
# li1 = ["data{}".format(i) for i in range(100)]
# print(li1)
#
# # 需求2：如何快速生成一个["data0","data2",...."data98"]的列表
# li2 = ["data{}".format(i) for i in range(100) if i%2 == 0]
# print(li2)

# 字典推导式
# dic = {key: value for i in item}

# 将字符串转换成字典
str1 = "a=1;b=2;c=3;d=4;e=5;f=6;g=7"
dic1 = {i.split("=")[0]: i.split("=")[1] for i in str1.split(";")}
# dic = {"{}".format(i).split("=")[0]: "{}".format(i).split("=")[1] for i in str1.split(";")}
print(dic1)

# {"data0": 1,"data1":2, "data2": 3}
dic2 = {"data{}".format(i): i + 1 for i in range(3)}
print(dic2)
