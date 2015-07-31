from room import Room
from stage import Stage
import yaml, os
		
class Scenario(object):
	def __init__(self, image=None, text = None):
		self.rooms = {}
		self.image = image
		self.text = text
		
	def add_room(self, room):
		self.rooms[room.name] = room
		
	def room(self, room):
		return self.rooms[room]		
		
	@staticmethod
	def from_data():
		
		data = yaml.load(open(os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			'scenario','data.yaml')))
		result = Scenario(data.get('image'), data.get('text'))
		for name, roomd in data['rooms'].items():
			room= Room(name, roomd.get('text'), roomd.get('image'))
			for name, staged in roomd['stages'].items():
				stage = Stage(name, staged.get('time'),
									staged.get('image', room.image),
									staged.get('text'),
									staged.get('hand'))
				room.add_stage(stage)
			result.add_room(room)
		
		return result
			
scenario = Scenario.from_data()