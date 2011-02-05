import os
from web import template

# Directory that contains the templates
templates_dir = "templates"

class View(object):
    def __init__(self, filename=None):
        if filename is not None:
            self._tpl = template.frender(os.path.join(templates_dir, filename))
        self._divs = {}

    def copy(self):
        """Returns a copy of the view"""
        new = View()
        new._tpl = self._tpl
        new._divs = self._divs.copy()
        return new

    def div(self, name, view):
        """Add subview"""
        self._divs[name] = view

    def render(self, *a, **ka):
        """Render view with data"""
        return self._tpl(self._divs, *a, **ka)

