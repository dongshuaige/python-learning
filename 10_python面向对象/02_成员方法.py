"""
演示成员方法
def 方法名(self,参数1,参数.....)
"""


class Student:
    name = None
    age = None

    # 构建无参成员方法
    def sayhi(self):
        print(f"大家好,我是{self.name},请大家多多关照")

    # 构建有参成员方法
    def sayhi2(self, msg):
        print(f"大家好,我是{self.name},{msg}")


stu_1 = Student()
stu_1.name = "周杰伦"
stu_1.sayhi()

stu_2 = Student()
stu_2.name = "林俊杰"
stu_2.sayhi()
