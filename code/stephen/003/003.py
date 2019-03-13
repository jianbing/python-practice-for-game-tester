#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/3/13 0013 下午 1:17
# @Author   : Stephen
# @Site     : 
# @File     : 003.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) Stephen 2019
# @Licence  :     <your licence>
import os

catalog = ""


class Folder():
    def __init__(self):
        if catalog == "":
            self.catalog = os.getcwd()
        else:
            self.catalog = catalog
        print self.catalog
        self.apk_list = os.listdir(self.catalog)

    def install(self):
        for i in self.apk_list:
            if str(i)[-4:0] == ".apk":
                os.system("adb install {0}".format(i))

z = Folder()
z.install()
