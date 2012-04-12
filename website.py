import cherrypy
from models import *
from lib.util import *

class Root(object):
    @cherrypy.expose
    def index(self):
        return render("index.html",{"name":"Richard"})

    @cherrypy.expose(alias="favicon.ico")
    def favicon(self):
        redirect("img/favicon.ico")
