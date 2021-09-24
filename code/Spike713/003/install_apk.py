#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     :
# @Author   : Spike713
# @Site     :
# @File     : install_apk.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:
# @Licence  :
import os

apkpath_list: list = []

def get_all_apk(file):

    for root, dirs, files in os.walk(file):  # 列出所有文件夹或文件名
        for f in files:
            filepath = os.path.join(root, f)  # os.path.join:将路径与文件或文件夹合在一起

        if os.path.basename(filepath).endswith('.apk'):  # 查找”.apk“结尾的文件
            apkpath_list.append(filepath)  # apkpath_list列表里加入上面查找到的文件
def install_apk(apklist: list):

    for apk in apklist:
        os.system('adb install -r ' + apk)


if __name__ == '__main__':
    get_all_apk('C:\\Users\\Administrator\\Desktop\\UAuto')
    print(apkpath_list)
    install_apk(apkpath_list)
