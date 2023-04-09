"""
演示distinct方法进行去重
"""

from util.Common_util import *

sc = gen_sc()

rdd = sc.parallelize([1, 2, 2, 3, 4, 5, 6, 6])
print(f"去重之前:{rdd.collect()}")

print(f"去重后:{rdd.distinct().collect()}")
