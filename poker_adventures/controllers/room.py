import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

from ..model import scenario

log = logging.getLogger(__name__)

class RoomController(BaseController):

    def index(self, room):
        try:
            c.main = scenario.room(room)
        except KeyError:
            abort(404)
        return render('room.mako')

    def fail(self, room):
        try:
            c.main = scenario.room(room)
        except KeyError:
            abort(404)
        return render('fail.mako')