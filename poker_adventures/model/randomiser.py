class Random(object):
	def __init__(self, prompt, rand=[]):
		self.rand = rand
		self.prompt = prompt
		self.template = 'random'
		
	def choose(self):
		import random
		print random
		print random.choice
		return random.choice(self.rand)