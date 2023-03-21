from gtk_imports import Gtk
from components.constants import *
from mainFunctions import insertComponentName

from mainFunctions import *

def generateMenu(stack):
    # Creating Main Box
    MenuBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("MENU PRINCIPAL") )
    ComponentName.set_size_request(-1, 200)

    # Creating buttons
    ChambresBtn = Gtk.Button(label="Lite des chambres")
    ReservationsBtn = Gtk.Button(label="Gérer les reservations")
    FacturesBtn = Gtk.Button(label="Factures")
    StatsBtn = Gtk.Button(label="Statistiques")
    QuitBtn = Gtk.Button("Quitter")

    # Binding callbacks
    ChambresBtn.connect("clicked", lambda y: changePage(stack, CHAMBRES))
    ReservationsBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))
    FacturesBtn.connect("clicked", lambda y: changePage(stack, FACTURES))
    StatsBtn.connect("clicked", lambda y: changePage(stack, STATS))
    QuitBtn.connect("clicked", Gtk.main_quit)

    # Stacking buttons in box
    MenuBox.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    MenuBox.pack_start(ChambresBtn, True, True, DEFAULT_BUTTON_PADDING)
    MenuBox.pack_start(ReservationsBtn, True, True, DEFAULT_BUTTON_PADDING)
    MenuBox.pack_start(FacturesBtn, True, True, DEFAULT_BUTTON_PADDING)
    MenuBox.pack_start(StatsBtn, True, True, DEFAULT_BUTTON_PADDING)
    MenuBox.pack_start(QuitBtn, True, True, DEFAULT_BUTTON_PADDING)

    
    return MenuBox