"""
练习案例1
"""
# 1.构建执行环境入口对象
from util.Common_util import gen_sc
import json

# 1. 构建执行环境入口对象
sc = gen_sc()

# 需求1 城市销售额排名
# 1.1读取文件
file_rdd = sc.textFile("../data/orders.txt")
# 1.2 取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
# 1.3 将json字符串转成字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
# 1.4 取出城市和销售额数据
# (城市,销售额)
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# 1.5 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b)
# 1.6按销售额聚合结果进行排序
result_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(f"需求1_的结果:{result_rdd.collect()}")
# 需求2: 全部城市有哪些商品类别在售卖
# 2 取出全部商品类别 并对对全部商品类别去重
all_category_rdd = dict_rdd.map(lambda x: x['category']).distinct()
print(f"需求2结果:{all_category_rdd.collect()}")
# 需求3 北京市有哪些商品类别在售卖
# 3.1 过滤北京市的数据
bj_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')
# 3.2 取出全部商品类别并去重
bj_category_rdd = bj_data_rdd.map(lambda x: x['category']).distinct()
print(f"需求3结果:{bj_category_rdd.collect()}")
