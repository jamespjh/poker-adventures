import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

log = logging.getLogger(__name__)

from ..model import scenario

class ScenarioController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/scenario.mako')
        # or, return a string
        return scenario.text
