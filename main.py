import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from components.mainMenu import MenuBox

PROGRAM_NAME = "Hotel Manager"

Win = Gtk.Window(title=PROGRAM_NAME)
Win.connect("destroy", Gtk.main_quit)

Win.add(MenuBox)

Win.maximize()
Win.show_all()
Gtk.main()