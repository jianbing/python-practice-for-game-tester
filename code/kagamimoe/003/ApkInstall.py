__author__ = 'kagami'

import os

apkpath_list = []

def get_all_apk(path: str)-> list:
	'''

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
	for apk in apklist:
		os.system('adb install -r' + apk)

if __name__ == '__main__':
	s = get_all_apk('/Users/kagami/Desktop/apk')
	print(apkpath_list)
	install_apk(apkpath_list)
