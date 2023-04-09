"""
判断语句的嵌套
"""
# print("欢迎来到动物园")
# if int(input("输入你的身高: ")) > 120:
#     print("你的身高大于120cm,不可以免费")
#     print("不过如果你的VIP等级高于3,可以免费游玩")
#
#     if int(input("请告诉我你的vip级别: ")) > 3:
#         print("恭喜你,你的vip级别大于3,可以免费游玩。")
#     else:
#         print("Sorry,你需要补票,10元")
# else:
#     print("欢迎你小朋友,可以免费游玩。")

age = int(input("请输入年龄:"))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("年龄达标了")
        if int(input("请输入入职时间:")) > 2:
            print("恭喜你,年龄和入职时间都达标了,可以领取礼物")
        elif int(input("请输入级别:")) > 3:
            print("恭喜你,年龄和级别达标,可以领取礼物")
        else:
            print("不好意思,尽管年龄达标,但是入职时间和级别都不达标")
    else:
        print("不好意思,年龄太大了")
else:
    print("不好意思,你是未成年,无法领取礼物")
