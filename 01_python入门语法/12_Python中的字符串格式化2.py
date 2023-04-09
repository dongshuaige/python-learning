"""
快速字符串格式化 字符串前面添加f 表示将要进行格式化 里面的变量用{} 括起来,不会进行精度控制
"""
name = "传值播客"
set_up_year = 2006
stock_price = 19.99
print(f"{name}成立于{set_up_year}年,今天的股价是:{stock_price}")
