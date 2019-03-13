#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/3/13 0013 下午 12:45
# @Author   : Stephen
# @Site     : 
# @File     : 002.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) Stephen 2019
# @Licence  :     <your licence>
"""
SVN环境未配置，暂时略过此题
"""

from prettytable import PrettyTable
import os


class Svn():
    def __init__(self):
        self.tb = PrettyTable()
        self.tb.field_names = ["ID", "指令"]
        self.tb.add_row([1, "SVN更新主干"])
        self.tb.add_row([2, "SVN还原主干"])
        self.tb.add_row([3, "启动游戏客户端"])
        self.tb.add_row([4, "打开主干目录"])
        print self.tb
        self.operation = input("选择指令:")
        if self.operation not in [1, 2, 3, 4]:
            print ("输入错误")

    def svn_oper(self):
        if self.operation == 1:
            os.system("svn update trunk")

a = Svn()
