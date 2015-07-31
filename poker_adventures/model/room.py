import inflection

from pylons import url
	
class Room(object):
	def __init__(self, name, text, title=None, image = None):
		self.name = name
		self.text = text
		self.image = image
		self.challenge = None
		self.title = title
		if not self.title:
			self.title = inflection.titleize(name)
			
		self.exits = {}
		
	def add_exit(self, route, room):
		self.exits[route] = room
		
	def add_challenge(self, cards, timer, success, fail, boni={}):
		self.success= success
		self.fail = fail
		self.boni = boni
		self.timer = timer
		self.boni["Each partner"]= 1
		self.challenge = cards