#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/3/13 0013 上午 10:44
# @Author   : Stephen
# @Site     : 
# @File     : 001.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) Stephen 2019
# @Licence  :     <your licence>
import re


class GM():
    def __init__(self, cmd_string):
        self.cmd_list = re.split("{{|}}", cmd_string)
        if "add_item " not in self.cmd_list:
            raise IOError("输入错误")

    def analysis(self):
        count = self.cmd_list[2]
        props = self.cmd_list[1]
        if "to" in props:
            operation = self.cmd_list[1].split(" ")
            start, end = int(operation[0]), int(operation[2])
            prop_list = [x for x in range(start, end + 1)]
            if "not" in props:
                remove_list = re.split(",", operation[4])
                for i in remove_list:
                    prop_list.remove(int(i))
        else:
            prop_list = self.cmd_list[1].split(",")
        command_list = map(lambda x: "add_item " + str(x) + count, prop_list)
        for i in command_list:
            print i


test1 = GM("add_item {{1001 to 1003}},10")
test1.analysis()
test2 = GM("add_item {{1001,1003,1006}},10")
test2.analysis()
test3 = GM("add_item {{1001 to 1005 not 1002,1003}},10")
test3.analysis()
