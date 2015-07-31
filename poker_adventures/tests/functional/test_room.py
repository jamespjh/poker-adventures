from poker_adventures.tests import *

class TestRoomController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='room', room='monaco', action='index'))
        # Test response...
