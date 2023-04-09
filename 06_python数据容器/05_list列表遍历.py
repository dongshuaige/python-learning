"""
演示使用while和for循环遍历列表
# 初始化列表
list() 或 []
列表中的元素可以被修改
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认是0
    # 每一次循环，将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量

    # 定义一个变量，用来标记列表的下标
    # 初始下标为0
    index = 0
    while index < len(mylist):
        # 通过index变量取出对应下标的元素
        element = mylist[index]
        print(f"列表的元素：{element}")

        # 至关重要：将循环变量（index）每一次循环都+1
        index += 1


def even_list_while_func(mylist):
    """
    使用for循环遍历列表并将偶数存入一个新的列表中
    :param mylist: 定义列表
    :return: None
    """
    # 定义一个空的列表
    even_list = list()
    index = 0
    # 遍历列表
    while index < len(mylist):
        element = mylist[index]
        if element % 2 == 0:
            even_list.append(element)
        index += 1
    print(f"使用while循环从列表:{mylist}中取出偶数,组成新列表:{even_list}")


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    mylist = [1, 2, 3, 4, 5]
    # for 临时变量 in 数据容器:
    for element in mylist:
        print(f"列表的元素有：{element}")


def even_list_for_func(mylist):
    """
    使用for循环遍历列表并将偶数存入一个新的列表中
    :param mylist: 定义列表
    :return: None
    """
    # 定义一个空的列表
    even_list = list()
    # 遍历列表
    for element in mylist:
        if element % 2 == 0:
            even_list.append(element)
    print(f"使用for循环从列表:{mylist}中取出偶数,组成新列表:{even_list}")


if __name__ == '__main__':
    # list_while_func()
    # list_for_func()
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_list_while_func(my_list)
    even_list_for_func(my_list)
