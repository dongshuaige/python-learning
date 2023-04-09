"""
多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。
函数(方法)形参声明接收父类对象
实际传入父类的子类对象进行工作
即:
以父类做定义声明
以子类做实际工作
用以获得同一行为, 不同状态

"""


class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪")


def make_noice(animal: Animal):
    animal.speak()


dog = Dog()
make_noice(dog)

cat = Cat()
make_noice(cat)
