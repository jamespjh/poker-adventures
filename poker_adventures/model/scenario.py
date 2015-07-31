from room import Room
import yaml, os
		
class Scenario(object):
	def __init__(self, name, image=None, text = None):
		self.rooms = {}
		self.name = name
		self.image = image
		self.text = text
		self.starts = []
		import inflection
		self.title = inflection.titleize(name)
		
	def add_room(self, room):
		self.rooms[room.name] = room
		
	def room(self, room):
		return self.rooms[room]
		
	def add_start(self, name):
		self.starts.append(self.rooms[name])

	@staticmethod
	def from_data():
		
		data = yaml.load(open(os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			'scenario','data.yaml')))

		scenario = Scenario(data['name'], 
						  data.get('image'), 
						  data.get('text'))
						  
		for name, roomd in data['rooms'].items():
			room= Room(name, 
				roomd.get('text'),
				roomd.get('title'),
				roomd.get('image', scenario.image)
				)
			scenario.add_room(room)
		
		for name in data['start']:
			scenario.add_start(name)
		
		for name, roomd in data['rooms'].items():
			room = scenario.room(name)
			for route, dname in roomd.get('exits', {}).items():
				target = scenario.room(dname)
				room.add_exit(route, target)
			if 'challenge' in roomd:
				challenged= roomd['challenge']
				print challenged.get('boni')
				room.add_challenge(
					challenged['cards'],
					challenged['timer'],
					scenario.room(challenged['success']),
					scenario.room(challenged['fail']),
					challenged.get('boni',{})
				)
		
		return scenario
			
scenario = Scenario.from_data()