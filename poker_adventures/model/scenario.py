from room import Room
import yaml, os
		
class Scenario(object):
	def __init__(self, name, image=None, text = None):
		self.rooms = {}
		self.name = name
		self.image = image
		self.text = text
		import inflection
		self.title = inflection.titleize(name)
		
	def add_room(self, room):
		self.rooms[room.name] = room
		
	def room(self, room):
		return self.rooms[room]		

	@staticmethod
	def from_data():
		
		data = yaml.load(open(os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			'scenario','data.yaml')))
		result = Scenario(data['name'], 
						  data.get('image'), data.get('text'))
		for name, roomd in data['rooms'].items():
			room= Room(name, 
				roomd.get('text'),
				roomd.get('title'),
				roomd.get('image'))
			result.add_room(room)
		
		return result
			
scenario = Scenario.from_data()