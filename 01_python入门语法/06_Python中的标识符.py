"""
标识符命名规则-内容限定
标识符命名中,只允许出现:
* 英文
* 中文
* 数字
* 下划线
这四类元素
其余任何内容都不被允许
注意:
  1. 不推荐使用中文
  2. 数字不可以开头
例如: a a_b _a _a_b a1 a_b_1
大小写敏感:
 Andy
 andy
不可使用关键字: 如False True None and as assert break class continue def del elif else except finally
"""
# 规则一 内容限定
b1 = "张三"
b_1 = b1
print(b_1)

# 规则二 大小写敏感
Andy = "安迪1"
andy = "安迪2"
print(Andy, andy)
# 规则三 关键字
false = False
true = True
print(false, true)

'''
标识符的命名规范:
变量名: 见名知意 下划线命名法 英文字母全小写法
类名
方法名
'''
# 见名知意
name = "张三"
age = 11
# 下划线命名
person_name = "小明"
person_age = 25
