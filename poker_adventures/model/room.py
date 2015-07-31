class Room(object):
	def __init__(self, name, text, image = None):
		self.name = name
		self.text = text
		self.image = image
		self.stages = {}
		
	def add_stage(self, stage):
		self.stages[stage.name] = stage
		
	def stage(self, stage):
		return self.stages[stage]