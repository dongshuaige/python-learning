"""
Python中的类型信息 type(xx)
"""
# 方式1 使用print直接输出类型信息
print(type("黑马"))
print(type(555))
print(type(5.45))

# 方式2 使用变量存储type语句的结果
name_type = type(15.3)
print("name_type:", name_type)

# 方式3 使用type() 语句, 查看变量中存储的数据类型
money = 50
print("变量存储的数据类型:", type(money))
