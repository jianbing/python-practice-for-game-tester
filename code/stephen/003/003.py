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

catalog = "E:\Code\\test_apk"  # 设置路径，如果不设置则为当前路径


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
            print i
            if str(i)[-4:] == ".apk":
                apk_catalog = self.catalog + "\\" + i
                print apk_catalog
                os.system("adb install -r {0}".format(apk_catalog))

z = Folder()
z.install()
