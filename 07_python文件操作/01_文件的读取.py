"""
演示对文件的读取
只读:"r"
可以改:"w"
追加: "a"
TextIOWrapper 对文本文件IO进行IO操作
"""
# 打开文件
import time

f = open("../data/测试.txt", "r", encoding="UTF-8")
print(f"文件类型{type(f)}")

# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")
print("-----------------------------------------------")
# 读取文件 - readLines()
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是:{line}")
# # 文件的关闭
# f.close()
# time.sleep(500000)
# with open as 别名语法操作文件 自动完成文件close
with open("../data/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

time.sleep(5000)
