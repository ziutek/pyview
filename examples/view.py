# vim: set encoding=utf-8 :
import pyview

# Change default templates directory
#pyview.templates_dir = "some_dir"

# Load layout and menu templates
layout = pyview.View("layout")
menu   = pyview.View("menu")

# Create the right column
right = pyview.View("right")
# Add view components
right.div("Info",       pyview.View("right_info"))
right.div("Commercial", pyview.View("right_commercial"))

# Create home view as layout copy.
home = layout.copy()
home.div("Menu",  menu)
home.div("Left",  pyview.View("left_home"))
home.div("Right", right)

# Create edit view.
edit = layout.copy()
edit.div("Menu",  menu)
edit.div("Left",  pyview.View("left_edit"))
edit.div("Right", right)
