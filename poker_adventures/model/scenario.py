from room import Room
from stage import Stage
import yaml, os
		
class Scenario(object):
	def __init__(self):
		self.rooms = {}
		
	def add_room(self, room):
		self.rooms[room.name] = room
		
	def room(self, room):
		return self.rooms[room]		
		
	@staticmethod
	def from_data():
		result = Scenario()
		data = yaml.load(open(os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			'scenario','data.yaml')))

		for name, roomd in data.items():
			room= Room(name, roomd.get('text'), roomd.get('background'))
			for name, staged in roomd['stages'].items():
				stage = Stage(name, staged.get('time'),
									staged.get('text'),
									staged.get('hand'))
				room.add_stage(stage)
			result.add_room(room)
		
		return result
			
scenario = Scenario.from_data()