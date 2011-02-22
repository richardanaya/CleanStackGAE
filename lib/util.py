from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import os
import cherrypy

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dirs = []
template_dirs.append(os.path.join(current_dir, '../templates'))

def get_template(name):
    env = Environment(loader = FileSystemLoader(template_dirs))
    try:
        return env.get_template(name)
    except TemplateNotFound:
        raise TemplateNotFound(name)

def render(name,params):
    return get_template(name).render(params)

def redirect(url):
    raise cherrypy.HTTPRedirect(url)
