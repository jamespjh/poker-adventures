import inflection

from pylons import url
	
class Room(object):
	def __init__(self, name, text, title=None, image = None):
		self.name = name
		self.text = text
		self.image = image
		self.obstacle = None
		self.title = title
		if not self.title:
			self.title = inflection.titleize(name)
		
	def add_obstacle(self, obstacle):
		self.obstacle = obstacle