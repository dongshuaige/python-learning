"""
演示filter
"""
from util.Common_util import gen_sc

sc = gen_sc()
# 过滤想要的数据进行保留
rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = rdd.filter(lambda x: x % 2 == 0)
print(rdd2.collect())
