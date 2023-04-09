"""
函数的嵌套调用
"""


def func_a():
    print("---2---")


def func_b():
    print("---1---")
    func_a()
    print("---3---")


func_b()
