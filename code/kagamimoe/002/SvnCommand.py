__author__ = 'kagami'

from prettytable import PrettyTable
import os

x = PrettyTable(["ID", "指令"])
x.add_row(['1', 'SVN更新主干'])
x.add_row(['2', 'SVN还原主干'])
x.add_row(['3', '启动游戏客户端'])
x.add_row(['4', '打开主干目录'])
print(x)
print("选择指令");

trunk_folder = 'D:/trunk'
trunk_client = 'D:/trunk/client.exe'

command = input();
if command == '1':
	os.system("svn update -r m trunk")
elif command == '2':
	os.system("svn update -r 200 trunk")
elif command == '3':
	os.startfile("trunk_client")
elif command == '4':
	os.startfile(trunk_folder)
else:
	print('命令输入错误')