"""
list列表操作案例
"""
# 定义一个列表并用变量接收
stu_list = [21, 25, 21, 23, 22, 20]
print(f"修改前的列表:{stu_list}")

# 追加一个数字31至列表的尾部
stu_list.append(31)
print(f"追加元素后的list:{stu_list}")
# 追加一个新列表[29,33,30]到列表尾部
my_list = [29, 33, 30]
stu_list.extend(my_list)
print(f"追加列表后的list:{stu_list}")

# 取出第一个元素
first_element = stu_list[0]
print(f"第一个元素{first_element}")

# 取出最后一个元素
last_element = stu_list[- 1]
print(f"最后一个元素{last_element}")

# 查找元素31在列表中的下标位置
stu_index = stu_list.index(31)
print(f"元素31在列表中的下标位置{stu_index}")
