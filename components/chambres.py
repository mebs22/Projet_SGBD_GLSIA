from gtk_imports import Gtk
from components.constants import *
from mainFunctions import insertComponentName
from mainFunctions import *

def generateChambres(stack):
    # Creating container
    ChambresBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("LISTE DES CHAMBRES") )
    ComponentName.set_size_request(-1, 200)


    # Creating Buttons
    BUTTONS = [
        ListFreeRoomsBtn,
        ListOccupiedRoomsBtn,
        BackBtn
    ] = [
        Gtk.Button(label="Chambres libres"),
        Gtk.Button(label="Chambres occupées"),
        Gtk.Button(label="Retour"),
    ]

    # Binding callbacks
    BUTTONS[0].connect("clicked", lambda y: changePage(stack, CHAMBRE_LIBRE))
    BUTTONS[1].connect("clicked", lambda y: changePage(stack, CHAMBRE_OCCUPEE))
    BUTTONS[2].connect("clicked", lambda y: goBack(stack))

    # Stacking elements
    ChambresBox.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    for BTN in BUTTONS:
        ChambresBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)

    return ChambresBox

def generateChambresLibres(stack): 
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("CHAMBRES LIBRES") )
    ComponentName.set_size_request(-1, 200)

    
    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, CHAMBRES))



    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)

    return Container


def generateChambresOccupees(stack): 
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("CHAMBRES OCCUPEES") )
    ComponentName.set_size_request(-1, 200)

    
    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, CHAMBRES))



    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)

    return Container
