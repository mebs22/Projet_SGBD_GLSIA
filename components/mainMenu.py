from gtk_imports import Gtk
import functions.mainMenuFunctions as MMFs
from components.constants import *


# Creating Main Box
MenuBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
GesHotelBtn = Gtk.Button(label="Gestion de l'hotel")

ChambresBtn = Gtk.Button(label="Chambres")

ClisBtn = Gtk.Button(label="Clients")

ReservationsBtn = Gtk.Button(label="Reservations")

FacturesBtn = Gtk.Button(label="Factures")

StatsBtn = Gtk.Button(label="Statistiques")

AideBtn = Gtk.Button(label="Aide")

QuitBtn = Gtk.Button(label="Quitter")

# Binding callbacks
QuitBtn.connect("clicked", Gtk.main_quit)
GesHotelBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, GESTION_HOTEL))
ChambresBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, CHAMBRES))
ClisBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, CLIENTS))
ReservationsBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, RESERVATIONS))
FacturesBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, FACTURES))
StatsBtn.connect("clicked", lambda y: MMFs.loadComponent(MenuBox, STATS))
AideBtn.connect("clicked", MMFs.showHelp)

# Stacking Buttons/Elements
MenuBox.pack_start(GesHotelBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ChambresBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ClisBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ReservationsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(FacturesBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(StatsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(AideBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(QuitBtn, True, True, DEFAULT_BUTTON_PADDING)