"""
for循环的基础应用
for 临时变量 in 待处理数据集:
    循环满足条件时的代码
"""
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1
print(f"itheima is a brand of itcast 共含有{count}个字母a")
