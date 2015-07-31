import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from poker_adventures.lib.base import BaseController, render

log = logging.getLogger(__name__)

from ..model import scenario

class ScenarioController(BaseController):

    def index(self):
        c.main = scenario
        return render('/scenario.mako')
