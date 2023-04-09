"""
演示继承 class 子类(父类1,父类2,xxx)
方式1：
调用父类成员
     使用成员变量：父类名.成员变量
     使用成员方法：父类名.成员方法(self)
方式2：
使用super()调用父类成员
     使用成员变量：super().成员变量
     使用成员方法：super().成员方法()

"""


class Phone:
    IMET = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("以4g网络运行")


class Phone2022(Phone):
    face_id = True

    def call_by_5g(self):
        print("切换为5g网络运行")
