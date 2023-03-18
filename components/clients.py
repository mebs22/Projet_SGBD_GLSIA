from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING


# Creating container
ClientsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
BUTTONS = [
    ListClisBtn,
    ListClisTodayOutBtn,
    ListClisReservedBtn,
    ListClisInHotelBtn,
    DeleteCliBtn,
    BackBtn
] = [
    Gtk.Button(label="Liste des clients"),
    Gtk.Button(label="Liste des clients qui sortant aujourd'hui"),
    Gtk.Button(label="Liste des clients reservés"),
    Gtk.Button(label="Liste des clients qui sont dans l'hotel"),
    Gtk.Button(label="Supprimer un client"),
    Gtk.Button(label="Retour"),
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    ClientsBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)
