from poker_adventures.tests import *

class TestScenarioController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='scenario', action='index'))
        # Test response...
