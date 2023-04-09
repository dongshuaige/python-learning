"""
python 中字符串3种定义方式
"" '' 三引号
"""
name = """
张三
今年
23岁
"""
print(type(name), name)
name = '黑马'
print(type(name), name)
name = "程序员"
print(type(name), name)

# 在字符串内包含双引号
name = '"黑马程序员"'
print(name)
name = "'王五'"
print(name)
# 使用转义字符\
name = "\"黑马\"" + ',\'IT\''
print(name)