#!/usr/bin/env python
# vim: set encoding=utf-8 :
from datetime import datetime
import web
import view


class MenuItem(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Page(object):
    # Global fields
    started = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hits = 0
    last_cli_addr = ""
    menu = (
        MenuItem("Home", "/"),
        MenuItem("Edit", "/edit"),
    )
    # You need to redefine the following fields in derived class
    _view = None
    title = None
    menu_selected = None
    left = None
    right = None


    def GET(self):
        cls = self.__class__
        cls.hits += 1
        yield self._view.render(self)
        try:
            cls.last_cli_addr = web.ctx.env["HTTP_X_FORWARDED_FOR"]
        except KeyError:
            try:
                cls.last_cli_addr = web.ctx.env["REMOTE_ADDR"]
            except KeyError:
                cls.last_cli_addr = "unknown"


class Home(Page):
    _view = view.home
    title = "Home page"
    menu_selected = 0
    left = (
        "This is a test service created in Python using <em>web.py</em> and "
        "its templating system.",
        "Please select another menu item!",
    )
    right = {
        "commercial":
            "A house is much better than a flat. So buy a new House today!"
    }


class Edit(Page):
    _view = view.edit
    title = "Edit page"
    menu_selected = 1
    left = (
        "Hello! You can modify this example.",
        "Open <em>main.py</em>, <em>view.py</em> or some template file in your"
        "editor and edit it.",
        "Then type: <code>$ ./main.py</code>",
    )
    right = {
        "commercial":
            "<a href='http://webpy.org/'>web.py</a> is a web framework for "
            "Python that is as simple as it is powerful. The web.py template "
            "language, called <em>Templetor</em> is designed to bring the "
            "power of Python to templates."
    }


urls = (
    "/edit", "Edit",
    "/",     "Home",
)


def main():
    view.init()
    web.application(urls, globals()).run()


if __name__ == "__main__":
    main()
