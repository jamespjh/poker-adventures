class Challenge(object):
	def __init__(self, success, fail, cards, time=5, boni=[]):
		self.success = success
		self.fail = fail
		self.cards = cards
		self.timer = time
		self.boni = boni
		self.template= 'challenge'
		