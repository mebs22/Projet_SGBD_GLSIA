from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING

# Creating mainBox
GesHotelBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating buttons
BUTTONS = [
    InfosBtn,
    EditHotelNameBtn,
    EditTarifsBtn,
    ResetHotelBtn,
    ColorsBtn,
    BackBtn
] = [
    Gtk.Button(label="Infos"), 
    Gtk.Button(label="Modifier nom hotel"), 
    Gtk.Button(label="Modifier tarifs"), 
    Gtk.Button(label="Reinitialiser l'hotel"), 
    Gtk.Button(label="Couleurs"), 
    Gtk.Button(label="Retour")
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    GesHotelBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)