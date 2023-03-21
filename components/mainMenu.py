from gtk_imports import Gtk
# import mainFunctions as MFs
from components.constants import *
import functions.mainMenuFunctions as MMFs
from mainFunctions import insertComponentName
# from components.chambres import ChambresBox
from components.chambres import generateChambres


# Page change function
def changePage(stack, child):
    stack.set_visible_child(child)

def goBack(stack):
    # Get index of current page
    index = stack.get_visible_child_name()
    # If current page is not  the first, go back to previous
    if index != "page1":
        previous_page = "page" + str(int(index[-1])-1)
        stack.set_visible_child_name(previous_page)



# Creating Main Box
MenuBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating stack for navigation
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)


# Creating SubComponent
ChambresPageTitle = Gtk.Label(label="Chambres")
ChambresBox = generateChambres(stack, ChambresPageTitle, goBack)


# Adding pages to stack
stack.add_titled(ChambresBox, "chambres", "Chambres")
print(stack)


# Generating Component name
ComponentName = Gtk.Label()
ComponentName.set_markup( insertComponentName("MENU PRINCIPAL") )
ComponentName.set_size_request(-1, 200)

# Creating Buttons
ChambresBtn = Gtk.Button(label="Chambres")

ReservationsBtn = Gtk.Button(label="Reservations")

FacturesBtn = Gtk.Button(label="Factures")

StatsBtn = Gtk.Button(label="Statistiques")

AideBtn = Gtk.Button(label="Aide")

QuitBtn = Gtk.Button(label="Quitter")

# Binding callbacks
QuitBtn.connect("clicked", Gtk.main_quit)
ChambresBtn.connect("clicked", lambda y: changePage(stack, ChambresBox))
ReservationsBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, RESERVATIONS))
FacturesBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, FACTURES))
StatsBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, STATS))
AideBtn.connect("clicked", MMFs.showHelp)

# Stacking Buttons/Elements
MenuBox.pack_start(ComponentName, True, True, 0)
MenuBox.pack_start(ChambresBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ReservationsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(FacturesBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(StatsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(AideBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(QuitBtn, True, True, DEFAULT_BUTTON_PADDING)