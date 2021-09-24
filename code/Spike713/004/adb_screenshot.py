#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     :
# @Author   : Spike713
# @Site     :
# @File     : adb_screenshot.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:
# @Licence  :
import os, time

def cap_screen_by_adb(folder):

	nowtime = time.localtime()
	times = time.strftime("%Y%m%d%H%M%S", nowtime)
	os.system("adb shell screencap -p /sdcard/screenshot" + times + ".png")
	os.system("adb pull /sdcard/screenshot" + times + ".png " + folder)

if __name__ == '__main__':
	cap_screen_by_adb("D:/bugreport")