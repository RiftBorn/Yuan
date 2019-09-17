"""
This script is for Yuan
"""


class YuanLi:
	
	def __init__(self, age=31, toefl_score=65, level=1):
		self.age = age
		self.toefl = toefl_score
		self._level = level
		self.hp = 1
		self.attack_point = 0
		self.reset_attributes()
		pass

	def answer(self):
		question = input('Please ask me a question: \na: Who is your favorite star?\nb: Which is your favorite sport?\nc: Which is your favorite anime?\n')
		answer_chart = {
			'a': 'Jacky Chain~',
			'b': 'Boxing',
			'c': 'Naroto',
		}
		print(answer_chart.get(question))

	def compute_init_attack(self):
		"""
		Computes the initial attack point for yuan
		@return: attack
		"""
		return 24 + (self._level / 10)**2

	def compute_init_hp(self):
		"""
		Computes the initial hp by level for yuan
		@return: hp
		"""
		return 20 + (self._level / 5)**2

	def die(self):
		print('Yuan: I faked my death...')

	def get_attacked(self, attack_point):
		"""
		Get attacked
		"""
		self.hp -= attack_point

	def get_attention(self):
		print('Come baby, my toefl_score is {}'.format(self.toefl))

	def reset_attributes(self):
		"""
		Compute the attributes for yuan
		"""
		self.hp = self.compute_init_hp()
		self.attack_point = self.compute_init_attack()

	def level_up(self):
		"""
		level up yuan
		"""
		self._level += 1
		self.reset_attributes()

	def talk(self):
		print("Hello, I'm Yuan Lee~~~~~\nI'm a {}-year old gay. Please love me.".format(self.age))
