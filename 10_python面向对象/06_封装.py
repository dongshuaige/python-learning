"""
将现实世界的属性和行为封装到类中,描述为成员变量和成员方法,从而完成对现实事物的描述
"""


class Phone:
    IMET = None  # 序列号
    producer = None  # 厂商

    __current_voltage = None  # 当前电压 私有属性

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            self.__keep_single_core()
            print("5g通话以开启")
        else:
            print("通话失败,电量不足")

    def __keep_single_core(self):
        print("让CPU以单核模式运行以节省电量")
