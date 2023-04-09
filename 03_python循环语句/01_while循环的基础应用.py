"""
while循环的基础应用
"""
# i = 0
# while i < 100:
#     print("小美,我喜欢你")
#     i += 1

# 1到100累加的和
# sum = 0
# i = 1
#
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1到100累加的和是:{sum}")

# 循环猜数字案例
import random

num = random.randint(1, 100)
count = 0
flag = True
while flag:
    count += 1
    guess_num = int(input("输入你要猜测的数字:"))
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜的大了")
        else:
            print("猜的小了")

print(f"总共猜了{count}次")


