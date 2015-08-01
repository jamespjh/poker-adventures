import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

from ..model import scenario

log = logging.getLogger(__name__)

class RoomController(BaseController):

    def __before__(self, room):
        try:
            c.main = scenario.room(room)
            c.obstacle = c.main.obstacle
        except KeyError:
            abort(404)

    def index(self, room):
        return render(c.obstacle.template+'.mako')

    def fail(self, room):
        return render('fail.mako')
        
    def submit(self, room):
        for requirement, choices in c.obstacle.requirements.items():
            if requirement not in request.params:
                return render('fail.mako')
            if not any(
                [choice in request.params[requirement].lower().strip() 
                    for choice in choices]):   
                return render('fail.mako')
        redirect(url(controller='room', room=c.obstacle.success, action='index'))