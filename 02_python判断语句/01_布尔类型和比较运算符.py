"""
布尔类型bool 真和假
布尔类型的字面量:
True 表示真(是、肯定)
False 表示假(否、否定)
"""

# 字面量定义
bool1 = True
bool2 = False
print(f"bool1变量的内容是:{bool1},类型是:{type(bool1)}")
print(f"bool1变量的内容是:{bool2},类型是:{type(bool2)}")
# 比较运算符的使用
#  == != > < >= <=
num1 = 10
num2 = 10
print(f"10 ==10的结果是:{num1 == num2}")
num1 = 10
num2 = 15
print(f"10 !=15的结果是:{num1 != num2}")

num1 = 10
num2 = 5
print(f"10 < 5的结果是:{num1 < num2}")