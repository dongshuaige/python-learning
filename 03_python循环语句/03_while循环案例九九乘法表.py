"""
九九乘法表
# print("",end="") prints输出不换行
print("Hello", end="")
print("World", end="")
# \t 制表符\t进行对齐
print("Hello\t World")
print("Hello\t Base")
"""
i = 1
while i <= 9:
    # 定义内层循环的
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    # print()输出一个空格
    print()
