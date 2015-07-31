import inflection

from pylons import url
	
class Room(object):
	def __init__(self, name, text, title=None, image = None):
		self.name = name
		self.text = text
		self.image = image

		self.title = title
		if not self.title:
			self.title = inflection.titleize(name)
		
		self.url = url(controller='room', room=self.name)
		self.exits = {}
		
	def add_exit(self, route, room):
		self.exits[route] = room