"""
演示类和对象
设计类,基于类创建对象,使用对象来完成类的工作
"""


# 定义类
class Clock:
    id = None  # 序列号
    price = None  # 零售价

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock_1 = Clock()
clock_1.ring()

clock_2 = Clock()
clock_2.ring()
