"""
pymsql 综合案例,读取文件,写入到mysql中
"""
from data_define import Record
from file_define import FileReader, TextFileReader, JsonFileReader
from pymysql import Connection

text_file_reader = TextFileReader("../data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("../data/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建链接
conn = Connection(host='81.69.228.105',  # 主机名host
                  port=3306,  # 端口号
                  user='root',  # 用户名
                  password='980114@.hgd',  # 密码
                  autocommit=True  # 自动提交
                  )
# 获得游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("py_sql")
# 组织sql语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province)" \
          f"values ('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    # 执行sql语句
    cursor.execute(sql)

# 关闭mysql 链接对象
conn.close()
