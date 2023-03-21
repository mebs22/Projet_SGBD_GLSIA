from gtk_imports import Gtk
from components.constants import *
from components.mainMenu import generateMenu
from components.chambres import generateChambres
from mainFunctions import *

PROGRAM_NAME = "Hotel Manager"

Win = Gtk.Window(title=PROGRAM_NAME)
Win.connect("destroy", Gtk.main_quit)



# Geneating and adding container
# AppBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
# Win.add(AppBox)

# Creating stack
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

# Creating pages
MainMenu = generateMenu(stack)
Chambres = generateChambres(stack)

# Adding pages to stack
stack.add_titled(MainMenu, MAIN, "Menu Principal")
stack.add_titled(Chambres, CHAMBRES, "Liste des chambres")


# Rendering
Win.add(stack)
Win.maximize()
Win.show_all()

Gtk.main()