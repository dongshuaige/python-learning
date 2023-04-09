"""
对象的定义
"""


# 1. 设计一个类(类比生活中:设计一张登记表)
class Student:
    name = None  # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None  # 记录学生国籍
    native_place = None  # 记录学生籍贯
    age = None  # 记录学生年龄


# 2. 创建一个对象(类比生活中:打印一张登记表)
stu_1 = Student()

# 3. 给对象属性赋值(填写表格)
stu_1.name = "zhangsan"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "河南南阳"
stu_1.age = 30

# 打印对象
print(f"姓名:{stu_1.name},性别:{stu_1.gender},国籍:{stu_1.nationality},籍贯:{stu_1.native_place},年龄:{stu_1.age}")
