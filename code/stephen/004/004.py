#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/3/13 0013 下午 2:16
# @Author   : Stephen
# @Site     : 
# @File     : 004.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:   (c) Stephen 2019
# @Licence  :     <your licence>
import os, time

# 输出文件夹， 如果不填写则为当前文件夹
output_file = ""
if output_file == "":
    output_file = os.getcwd()

file_name = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/%s.png" % file_name)
os.system("adb pull /sdcard/%s.png %s" % (file_name, output_file))
