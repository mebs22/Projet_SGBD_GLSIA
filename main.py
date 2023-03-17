import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# from testfile import openWindow

# Creating window
Win = Gtk.Window(title='Hotel Manager System')


# Creating child elements
Bty = Gtk.Button(label="Click me bitch")

# Binding callbacks (event handlers)
Win.connect("destroy", Gtk.main_quit)
Bty.connect("clicked", lambda x: openWindow()) 

# Binding elements
Win.add(Bty)

# Loading window
Win.show_all()
Win.maximize()
Gtk.main()