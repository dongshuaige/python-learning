"""
文件相关的类定义
"""
import json

from data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据,读到的每一条数据都转换为Record对象,将他们都封装为list内返回即可"""
        pass


# 读取文本文件
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量,记录文件的路径

    # 复习(实现抽象方法) 父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []

        for line in f.readlines():
            line = line.strip()  # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量,记录文件的路径

    # 复习(实现抽象方法) 父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("../data/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("../data/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for i in list1:
        print(i)

    for i in list2:
        print(i)
