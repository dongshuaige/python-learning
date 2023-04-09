"""
演示flatMap方法
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
    rdd = sc.parallelize(["itcatst beijing", "itcatst shanghai", "itcatst hangzhou", "itcatst changsha"])

    # ['itcatst', 'beijing', 'itcatst', 'shanghai', 'itcatst', 'hangzhou', 'itcatst', 'changsha']
    print(rdd.flatMap(lambda x: x.split(" ")).collect())
