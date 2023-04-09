"""
字符串格式化 使用%s 占位符将变量转换为字符串
%s 将内容转为字符串,放入占位位置
%d 将内容转为整数,放入占位位置
%f 将内容转换为浮点数,放入占位位置
"""
# 通过占位的形式完成拼接(数字与字符串)
class_num = 57
avg_salary = 16381
message = "Python大数据学科,北京%s期,毕业平均工资: %s" % (class_num, avg_salary)
print(message)

# %s %d %f 使用
name = "传值播客"
set_up_year = 2006
stock_price = 19.99
message = "%s成立于%d年,今天的股价是:%f" % (name, set_up_year, stock_price)
print(message)