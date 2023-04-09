"""
演示RDD的map成员成员方法
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
    rdd = sc.parallelize([1, 2, 3, 4, 5])


    # 通过map方法将全部数据都乘以10

    def data_func(data):
        return data * 10


    print(rdd.map(data_func).collect())
    # f(T)->(U)
    print(rdd.map(lambda data: data * 10).collect())
