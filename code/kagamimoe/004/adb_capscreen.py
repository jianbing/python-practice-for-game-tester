__author__ = 'kagami'

import os, time

def cap_screen_by_adb(folder: str):
	'''
	使用adb截图 并且用当天日期+时间命名 并且支持导入到指定文件夹
	:param folder:
	:return:
	'''
	nowtime = time.localtime()
	times = time.strftime("%Y%m%d%H%M%S", nowtime)
	os.system("adb shell screencap -p /sdcard/screenshot" + times + ".png")
	os.system("adb pull /sdcard/screenshot" + times + ".png" + folder)

if __name__ == '__main__':
	cap_screen_by_adb("D:/bugreport")