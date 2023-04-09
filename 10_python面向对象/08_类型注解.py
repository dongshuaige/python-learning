"""
类型注解
变量: 类型 如 var_1 : int = 10
注释后: type: 类型
"""
var_1: int = 10
var_2: str = "nihao"
var_3: list = ["nihao"]
var_4: set = {1, 2, 3}
var_5: dict = {"age": 12}
var_6: tuple = (1, 2, 3)

age = 12  # type:int


def add(x: int, y: int) -> int:
    return x + y


def func(data: list[int]) -> list[int]:
    pass


# 联合类型注解Union[类型, ......, 类型]
from typing import Union

my_list: list[Union[str, int]] = [1, 2, "it", "boy"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}
