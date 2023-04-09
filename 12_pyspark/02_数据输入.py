"""
演示通过PySpark代码加载数据,即数据输入
"""
from pyspark import SparkConf, SparkContext

# 创建SparkConf 类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 通过SparkContext的parallelize成员方法，将Python数据容器转换为RDD对象
# rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
# rdd1 = sc.parallelize((1, 2, 3, 4, 5, 6))
# rdd2 = sc.parallelize({"age": 12})
# rdd3 = sc.parallelize({1, 2, 3, 4, 5, 6})
#
# # 打印RDD内容 通过collect()
# print(rdd.collect())
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# 通过SparkContext的textFile成员方法，读取文本文件得到RDD对象
rdd = sc.textFile("D:/MyWorkspace/pyproject/python-learning/txt/word.txt")
print(rdd.collect())
# 关闭SparkContext对象
sc.stop()
