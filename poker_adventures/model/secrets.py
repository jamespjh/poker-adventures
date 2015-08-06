class Secrets(object):
	def __init__(self, success, fail, requirements={}, special = {},
			failtext="", 
			failcontinue=""):
		self.success = success
		self.fail = fail
		self.requirements = requirements
		self.template = 'secrets'
		self.special = special
		self.failtext = failtext or "You have failed."
		self.failcontinue = failcontinue or "Click here to let someone else try"
		
	def validate(self, response):
		for requirement, choices in self.requirements.items():
			if requirement not in response:
				return False
			if not any(
				[choice in response[requirement].lower().strip() 
					for choice in choices]):   
				return False
		return True
		
	def direct(self, response):
		for answer in response.values():
			for special_answer in self.special:
				if special_answer in answer.lower().strip():
					return self.special[special_answer]
		return self.success