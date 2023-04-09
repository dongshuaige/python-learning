"""
if 条件1:
    xx
elif 条件2:
    yy
elif 条件3:
    cc
elif xx:
    ...
else:
    oo
"""
print("欢迎来到动物园")
if int(input("请输入你的身高(cm):")) <= 120:
    print("您的身高未超出120cm,可以免费游玩")
elif int(input("请输入你的vip级别(1~5):")) > 3:
    print("您的vip级别大于3,可以免费游玩")
elif int(input("告诉我今天是几号:")) == 1:
    print("今天是免费日,可以免费游玩")
else:
    print("不好意思,所有条件都不满足,需要购票10元")
print("祝您游玩愉快")
