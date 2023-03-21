from gtk_imports import Gtk
from components.constants import *
from mainFunctions import changePage
from mainFunctions import insertComponentName

def generateFactures(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("FACTURES") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, MAIN))

    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)



    return Container
