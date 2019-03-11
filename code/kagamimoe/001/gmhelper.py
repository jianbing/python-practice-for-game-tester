__author__ = 'kagami'


class Gmhelper():


	def check_command_is_legal(self, command: str):
		'''
		检查字符串是否符合规定格式
		:param command:
		:return: True表示合法 False表示不合法
		'''
		self.command = command
		if '{' and '}' not in command:
			print('GM命令格式错误,缺少大括号,请重新检查')
			return False
		if ',' not in command:
			print('GM命令格式错误,缺少逗号,请重新检查')
			return False
		return True

	def add_item_normal(self, command: str):
		'''
		把指定字符串转换成GM命令
		:param command: add_item {{1001 to 1003}},10 这种字符串
		:return:
		'''
		self.command = command
		if self.check_command_is_legal(self.command):
			split = self.command.index(',')
			start = self.command.index('{{')
			end = self.command.index('}}')
			data = self.command[start + 2:end]
			number_list = data.split('to')
			number_list[0] = int(number_list[0])
			number_list[1] = int(number_list[1])
			if number_list[0] >= number_list[1]:
				print('后面的数字需要大于前面的数字')
			for i in range(number_list[0], number_list[1]):
				print('add item ' + str(i) + self.command[split:])

	def add_item_by_list(self, command: str):
		'''
		把指定字符串转换成GM命令
		:param command: add_item {{1001,1003,1006}},10
		:return:
		'''
		self.command = command
		if self.check_command_is_legal(self.command):
			split = self.command.index('}},')
			start = self.command.index('{{')
			end = self.command.index('}}')
			data = self.command[start + 2:end]
			number_list = data.split(',')
			for i in number_list:
				print('add item ' + str(i) + self.command[split + 2:])

	def add_item_by_list_and_join(self, command: str):
		'''
		把指定字符串转换成GM命令
		:param command:add_item {{1001 to 1005 not 1002,1003}},10
		:return:
		'''
		self.command = command
		if self.check_command_is_legal(self.command):
			split = self.command.index('}},')
			start = self.command.index('{{')
			end = self.command.index('}}')
			data = self.command[start + 2:end]
			command_list = data.split('not ')
			number_list = command_list[0].split('to')
			ban_list = command_list[1].split(',')
			number_list[0] = int(number_list[0])
			number_list[1] = int(number_list[1])
			print(ban_list)
			if number_list[0] >= number_list[1]:
				print('后面的数字需要大于前面的数字')
			for i in range(number_list[0], number_list[1] + 1):
				if str(i) not in ban_list:
					print('add item ' + str(i) + self.command[split + 2:])


if __name__ == '__main__':
	str1 = 'add_item {{1001 to 1003}},10'
	str2 = 'add_item {{1001,1003,1006}},10'
	str3 = 'add_item {{1001 to 1005 not 1002,1003}},10'
	gm = Gmhelper()
	gm.add_item_normal(str1)
	gm.add_item_by_list(str2)
	gm.add_item_by_list_and_join(str3)