"""
演示python pymysql库的基本操作
"""

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
conn.select_db("test")  # 先选择数据库
# 使用游标对象,执行sql语句
# cursor.execute("CREATE TABLE test_pymysql(id int,info varchar(255))")
# cursor.execute("select * from courses")
# 获取查询结果 游标对象.fetchall()得到全部的查询结果封装入元组内
# results: tuple = cursor.fetchall()
# for result in results:
#     print(result)
cursor.execute("insert into courses values(6,'Python',200,now(),9)")
# 手动提交
# conn.commit()
conn.close()
