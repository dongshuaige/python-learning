"""
函数: 是组织好,可重复使用的,用来实现特定功能的代码段
"""
name = "it cast"
length = len(name)
print(length)


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(name)
