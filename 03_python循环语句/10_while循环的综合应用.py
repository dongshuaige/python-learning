"""
while循环的综合案例
"""
money = 10000
# for 循环对员工发放工资
for i in range(1, 21):
    import random

    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分{score},不满足,不发工资,下一位")
        # continue 跳过发放
        continue
    # 判断余额是否充足
    if money >= 1000:
        money -= 1000
        print(f"员工{i},满足条件发放工资1000,公司账户余额:{money}")
    else:
        print(f"余额不足,当前余额:{money}元,不足以发工资,不发了,请下个月来领取")
        # break结束发放
        break
