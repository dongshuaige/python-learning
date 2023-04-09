"""
演示其他内置方法 __str__ __le__ __eq__ __lt__
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象: name:{self.name},age:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


if __name__ == '__main__':
    stu = Student("周杰伦", 31)
    stu1 = Student("周杰伦", 31)
    print(stu == stu1)
