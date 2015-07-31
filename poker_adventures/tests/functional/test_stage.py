from poker_adventures.tests import *

class TestStageController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='stage', action='index'))
        # Test response...
