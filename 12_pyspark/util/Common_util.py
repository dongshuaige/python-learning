from pyspark import SparkContext, SparkConf
import os


def gen_sc():
    os.environ['PYSPARK_PYTHON'] = "D:/Tools/python/python.exe"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    return sc
