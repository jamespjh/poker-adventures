import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

from ..model import scenario

log = logging.getLogger(__name__)

class RoomController(BaseController):

    def index(self, room):
        # Return a rendered template
        #return render('/room.mako')
        # or, return a string
        try:
            room = scenario.room(room)
        except KeyError:
            abort(404)
        return room.name
