# @Author  : ShiRui
import itertools


class CreatePasswordTable:

	def __init__(self, word="123456789"):

		self.ite = itertools.product(word, repeat=4)
		self.dic = open("password.txt", 'a')

	def create(self):

		for i in self.ite:

			self.dic.write("".join(i))
			self.dic.write("".join('\n'))

		self.dic.close()


if __name__ == "__main__":

	create = CreatePasswordTable()
	create.create()
