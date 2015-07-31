import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

log = logging.getLogger(__name__)

class StageController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/stage.mako')
        # or, return a string
        return 'Hello World'
