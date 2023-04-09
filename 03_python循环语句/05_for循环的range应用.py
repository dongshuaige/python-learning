"""
range应用:
语法1:
range(num) 获取一个从0开始,到num结束的数字序列(不含num)
如range(5) 获取的数据是[0,1,2,3,4]
语法2:
range(num1,num2) 获取一个从num1开始,到num2结束的数字序列(不含num2)
语法3:
range(num1,num2,step) 获取一个从num1开始,到num2结束的数字序列(不含num2)
数字之间的步长,以step为准(step默认为1)
如range(5,10,2) 取得的数据是[5,7,9]
"""
# 语法1 range(num) 获取一个从0开始,到num结束的数字序列(不含num)
# for x in range(10):
#     print(f"{x}\t", end='')
# print()
# 语法2 range(num1,num2) 获取一个从num1开始,到num2结束的数字序列(不含num2)
# for x in range(5, 10):
#     print(f"{x}\t", end='')
# print()
# 语法3 range(num1,num2,step) 获取一个从num1开始,到num2结束的数字序列(不含num2),数字之间的步长,以step为准(step默认为1)
# for x in range(5, 15, 2):
#     print(f"{x}\t", end='')
count = 0
num = 100
for x in range(1, num):
    if x % 2 == 0:
        count += 1
print(f"1到100(不含100)范围内,有{count}个偶数")
