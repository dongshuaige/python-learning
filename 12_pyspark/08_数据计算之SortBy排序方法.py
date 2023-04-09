"""
演示sortBy排序方法
"""
from util.Common_util import *

# 1. 构建执行环境入口对象
sc = gen_sc()

# 2. 读取数据文件
rdd = sc.textFile("D:/MyWorkspace/pyproject/python-learning/12_pyspark/txt/hello.txt")
# 3.取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 4.将所有单词都转成二元元组,单词为Key,Value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 5.分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 排序
sorted_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(sorted_rdd.collect())
