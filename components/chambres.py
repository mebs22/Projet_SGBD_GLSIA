from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING
from mainFunctions import insertComponentName
# from mainFunctions import goBack

def generateChambres(stack, pageTitle, goBack):
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
    BUTTONS[len(BUTTONS)-1].connect("clicked", lambda y: goBack(stack))

    # Stacking elements
    # ChambresBox.pack_start(pageTitle, True, True, DEFAULT_BOX_SPACING)
    ChambresBox.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    for BTN in BUTTONS:
        ChambresBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)

    return ChambresBox
