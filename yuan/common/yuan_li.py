"""
This script is for Yuan
"""
import random


class YuanLi:
	
	def __init__(self, age=31, toefl_score=65):
		self.age = age
		self.toefl = toefl_score
		self._level = 1
		pass

	def talk(self):
		print("Hello, I'm Yuan Lee~~~~~\nI'm a {}-year old gay. Please love me.".format(self.age))

	def get_attention(self):
		print('Come baby, my toefl_score is {}'.format(self.toefl))

	def answer(self):
		question = input('Please ask me a question: \na: Who is your favorite star?\nb: Which is your favorite sport?\nc: Which is your favorite anime?\n')
		answer_chart = {
			'a': 'Jacky Chain~',
			'b': 'Boxing',
			'c': 'Naroto',
		}
		print(answer_chart.get(question))	

	def fight(self):
		random.seed()
		random_num = random.randint(0,10)
		if random_num > 5:
			self._level += 1
		else:
			 self.die()
		pass

	def die(self):
		print('I faked my death...')

