class Secrets(object):
	def __init__(self, success, fail, requirements={}):
		self.success = success
		self.fail = fail
		self.requirements = requirements
		self.template = 'secrets'