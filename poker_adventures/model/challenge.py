class Challenge(object):
	def __init__(self, success, fail, cards, time, boni={}):
		self.success = success
		self.fail = fail
		self.cards = cards
		self.timer = time
		self.boni = {}
		self.boni["Each partner"]= 1
		self.template= 'challenge'
		