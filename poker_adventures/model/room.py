import inflection
		
class Room(object):
	def __init__(self, name, text, title=None, image = None):
		self.name = name
		self.text = text
		self.image = image

		self.title = title
		if not self.title:
			self.title = inflection.titleize(name)