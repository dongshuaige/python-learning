"""
演示python pymysql 查询数据并写入文件中
"""
import json

from pymysql import Connection

# 简历链接
conn = Connection(host='81.69.228.105',  # 主机名host
                  port=3306,  # 端口号
                  user='root',  # 用户名
                  password='980114@.hgd',  # 密码
                  autocommit=True  # 自动提交
                  )
# 打印mysql连接信息
# print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
conn.select_db("py_sql")  # 先选择数据库
# 使用游标对象,执行sql语句
cursor.execute("select * from orders")
# 获取查询结果 游标对象.fetchall()得到全部的查询结果封装入元组内
results: tuple = cursor.fetchall()
# 打开文件
f = open("D:/MyWorkspace/pyproject/python-learning/数据库中数据写入.txt", "a", encoding="UTF-8")
data_dict = {}
for result in results:
    data_list = json.loads(json.dumps(result, default=str, ensure_ascii=False))
    data_dict["data"] = data_list[0]
    data_dict["order_id"] = data_list[1]
    data_dict["money"] = data_list[2]
    data_dict["province"] = data_list[3]
    f.write(f"{str(data_dict)}\n")
# 手动提交
# conn.commit()
f.close()
conn.close()
