def test_derivation():
    """
    推导式的格式：
    [处理迭代中的每一个元素  for语句   条件判断]
    """
    # 返回1~100所有的偶数   [2,4,6,8.....100]
    result = []
    for i in range(1, 101):
        if i % 2 == 0:
            result.append(i)
    print(result)

    print([i for i in range(1, 101) if i % 2 == 0])  # 列表推导式   列表解析

    print(["第" + str(i) + "题" for i in range(1, 10)])

    # 还可以应用于字典的解析
    cookie = "_ga=GA1.2.930106050.1598708338; Hm_lvt_39b794a97f47c65b6b2e4e1741dcba38=1601376712,1601378209,1601378225,1601378754; __gads=ID=d51165f71c40f9ea:T=1598708341:R:S=ALNI_MZNqeB0nRFuLFMHnaiqkRUxBzf4FQ; UM_distinctid=176b8fb1876443-00bac4ce20b2-3323767-1fa400-176b8fb18776f; CNZZDATA1278819128=727475643-1609418695-https%253A%252F%252Fwww.baidu.com%252F%7C1609418695; Hm_lvt_e2fcb48ccb07c3714ef5b2d8ebbe5bac=1609421232; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8EklyHYHyB5Oj4onWtxTnxZK-SyYDsAq4COxRCEyMCXVnz1Dm-qDFJUvwPYvokG_RRwY17vcaB5If8VM7G0ko8cvd0RmS5frC7yOg0-xGo7Xzim9enGJ45ZqPXn24gU1XorwYZg3T2KdYGRMNKBQitw; _gid=GA1.2.1426547664.1614343372"
    s = """ hello """
    s1 = "hello"
    s2 = 'hello'

    # cookie格式：  cookie键1=cookie值1；键2=值2；键3：值3；.....
    # cookie新格式： {键1：值1,键2：值2......}
    new_cookie = {}
    for item in cookie.split(';'):  # 先用；分割cookie
        s = item.split('=')  # 用 = 分割
        new_cookie[s[0]] = s[1]  # =左边作为键，=右边作为值，添加到new_cookie字典中
    print(new_cookie)  # 输出new_cookie
    # 字典推导式  字典解析 格式如下：
    # {键：值  for语句}
    print({item.split('=')[0]: item.split('=')[1] for item in cookie.split(';')})


if __name__ == '__main__':
    test_derivation()
