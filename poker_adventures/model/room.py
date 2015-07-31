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
		
		self.url = url(controller='room', room=self.name)
		self.exits = {}
		
	def add_exit(self, route, room):
		self.exits[route] = room
		
	def add_challenge(self, cards,  success, fail, boni={}):
		self.exits['Click here if you succeed.'] = success
		self.exits['Click here if you fail.'] = fail
		self.boni = boni
		self.boni["Each partner"]= 1
		self.challenge = cards