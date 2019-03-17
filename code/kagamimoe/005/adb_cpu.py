__author__ = 'kagami'

import os
from pyecharts import Bar


def get_mem_by_packagename(packagename: str):
	'''
	使用adb命令 获取内存使用信息
	:param folder:
	:return:
	'''
	s = os.popen("{}{}".format("adb shell dumpsys meminfo", packagename))
	mem_info = s.read()
	print(mem_info)

def get_cpu_by_packagename(packagename: str):
	'''
	使用adb命令 获取cpu使用信息
	:return:
	'''
	s = os.popen("{} {}".format("adb shell top -m 10 | FINDSTR ", packagename))
	cpu_info = s.read()
	print(cpu_info)



if __name__ == '__main__':
	# cap_screen_by_adb("D:/bugreport")
	bar = Bar("我的第一个图表", "这里是副标题")
	bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
	bar.render()    # 生成本地 HTML 文件
