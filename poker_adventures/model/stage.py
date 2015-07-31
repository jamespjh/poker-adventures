class Stage(object):
	def __init__(self, name, image, time, text, hand):
		self.name = name
		self.time = time
		self.text = text
		self.hand = hand
		self.background = image
		