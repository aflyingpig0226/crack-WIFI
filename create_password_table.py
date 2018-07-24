# @Author  : ShiRui
import itertools  # 引入迭代器


class CreatePasswordTable:  # 创建wifi密码表

	def __init__(self, word="123456789"):  # word是密码表生成数，如果密码表更加复杂的话，可以加入英文字母

		self.ite = itertools.product(word, repeat=4)  # repeat是生成几位数字的密码表，一般来说是八位，因为八位跑下来很大，所以这里示例是四位
		self.dic = open("password.txt", 'a')  # 打开密码表 "a"是追加写入或则没有文件就创建

	def create(self):

		for i in self.ite:

			self.dic.write("".join(i))  # 因为生成的密码是元祖，用split去切割麻烦，这里用join来连接
			self.dic.write("".join('\n'))  # 因为需要换行，所以还有加入一个‘\n'

		self.dic.close()


if __name__ == "__main__":

	create = CreatePasswordTable()
	create.create()
