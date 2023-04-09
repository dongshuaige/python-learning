"""
演示数据输出
"""
from util.Common_util import *

# 1. 构建执行环境入口对象
sc = gen_sc()
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# reduce 算子 对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)
# take 算子 取出前n个元素
top_list = rdd.take(3)
print(top_list)
# count 算子 rdd中的元素个数
rdd_count = rdd.count()
print(f"rdd中有{rdd_count}个元素")
sc.stop()
