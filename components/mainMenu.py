import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import functions.mainMenuFuncitions as MMFs

# CONSTANTS
DEFAULT_BUTTON_PADDING = 5
DEFAULT_BOX_SPACING = 10

# Creating Main Box
MenuBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
GesHotelBtn = Gtk.Button(label="Gestion de l'hotel")

ChambresCliBtn = Gtk.Button(label="Chambres")

ClisBtn = Gtk.Button(label="Clients")

ReservationsBtn = Gtk.Button(label="Reservations")

FacturesBtn = Gtk.Button(label="Factures")

StatsBtn = Gtk.Button(label="Statistiques")

AideBtn = Gtk.Button(label="Aide")

QuitBtn = Gtk.Button(label="Quitter")

# Binding callbacks
QuitBtn.connect("clicked", Gtk.main_quit)


# Stacking Buttons
MenuBox.pack_start(GesHotelBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ChambresCliBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ClisBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(ReservationsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(FacturesBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(StatsBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(AideBtn, True, True, DEFAULT_BUTTON_PADDING)
MenuBox.pack_start(QuitBtn, True, True, DEFAULT_BUTTON_PADDING)