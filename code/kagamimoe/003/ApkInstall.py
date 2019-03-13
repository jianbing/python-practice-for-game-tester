__author__ = 'kagami'

import os

apkpath_list = []

def get_all_apk(path: str)-> list:
	'''
	遍历文件目录把所有apk的路径存入list
	:param path:
	:return:
	'''
	for file in os.listdir(path):
		filepath = os.path.join(path, file)
		if os.path.isfile(filepath):
			if os.path.basename(filepath).endswith('.apk'):
				apkpath_list.append(filepath)
			else:
				continue
		elif os.path.isdir(filepath):
			get_all_apk(filepath)

def install_apk(apklist: list):
	'''
	遍历存放apk绝对路径的list 调用adb命令
	:param apklist:
	:return:
	'''
	for apk in apklist:
		os.system('adb install -r' + apk)

if __name__ == '__main__':
	s = get_all_apk('/Users/kagami/Desktop/apk')
	print(apkpath_list)
	install_apk(apkpath_list)
