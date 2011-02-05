# vim: set encoding=utf-8 :
import sys
sys.path.append("..")
import pyview


# Web pages
home = None
edit = None


def init(templates_dir=None):
    global home, edit

    # Change default templates directory
    if templates_dir is not None:
        pyview.templates_dir = templates_dir

    # Load layout and menu templates
    layout = pyview.View("layout.html")
    menu   = pyview.View("menu.html")

    # Create the right column
    right = pyview.View("right.html")
    # Add view components
    right.div("Info",       pyview.View("right/info.html"))
    right.div("Commercial", pyview.View("right/commercial.html"))

    # Create home view as layout copy.
    home = layout.copy()
    home.div("Menu",  menu)
    home.div("Left",  pyview.View("left/home.html"))
    home.div("Right", right)

    # Create edit view.
    edit = layout.copy()
    edit.div("Menu",  menu)
    edit.div("Left",  pyview.View("left/edit.html"))
    edit.div("Right", right)
