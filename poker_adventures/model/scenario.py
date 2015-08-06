from room import Room
from secrets import Secrets
from decision import Decision
from challenge import Challenge

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
			
			if 'exits' in roomd:
				obstacle = Decision(
					roomd['exits']
				)
				
			if 'cards' in roomd:
				obstacle = Challenge(
						roomd['success'],
						roomd['fail'],
						roomd['cards'],
						roomd.get('timer',5),
						roomd.get('boni',[])
				)
						
			if 'requirements' in roomd:
				obstacle = Secrets(
					roomd['success'],
					roomd['fail'],
					roomd['requirements'],
					roomd.get('special',{})
				)

			room.add_obstacle(obstacle)
		
		return scenario
			
scenario = Scenario.from_data()