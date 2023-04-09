"""
演示RDD reduceByKey方法
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Tools/python/python.exe"

if __name__ == '__main__':
    # 创建SparkConf 类对象
    conf = SparkConf().setMaster("local[*]").setAppName("create add")
    # 基于SparkConf类对象创建SparkContext类对象
    sc = SparkContext(conf=conf)

    # 准备一个RDD
    rdd = sc.parallelize([("a", 1), ("b", 1), ("c", 1), ("a", 2), ("b", 1), ("c", 3)])

    # [('b', 2), ('a', 3), ('c', 4)]
    print(rdd.reduceByKey(lambda a, b: a + b).collect())
