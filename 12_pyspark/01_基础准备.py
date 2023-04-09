"""
演示获取PySpark的执行环境入库对象:SparkContext
并通过SparkContext对象获取当前PySpark的版本
通过SparkContext对象，完成数据输入
输入数据后得到RDD对象，对RDD对象进行迭代计算
最终通过RDD对象的成员方法，完成数据输出工作
"""

# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf 类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext 对象的运行(停止pySpark程序)
sc.stop()
