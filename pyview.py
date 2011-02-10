import os
from web import template

# Directory that contains template files
templates_dir = "templates"

class View(object):
    def __init__(self, filename=None, glob=None, **keywords):
        """If glob isn't None it will be added to keywords as 'globals'"""
        if filename is not None:
            if glob is not None:
                keywords["globals"] = glob
            self._tpl = template.frender(os.path.join(templates_dir, filename),
                                         **keywords)
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

