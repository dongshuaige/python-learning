"""
演示构造方法: __init__(self,属性...)
"""


class Student:
    # 可以省略
    # name = None
    # age = None
    # tel = None
    # 构建类时传入的参数会自动提供给__init__方法
    # 构建类的时候__init__ 方法会自动执行
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")


stu = Student("张三", 25, "13588565")
