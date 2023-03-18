from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING


# Creating container
ChambresBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
BUTTONS = [
    ListRoomsBtn,
    ListFreeRoomsBtn,
    ListOccupiedRoomsBtn,
    ListReservedRoomsBtn,
    EditRoomClassBtn,
    EcoRooms,
    StandingRooms,
    BusinessRooms,
    BackBtn
] = [
    Gtk.Button(label="Liste des chambres"),
    Gtk.Button(label="Liste des chambres libres"),
    Gtk.Button(label="Liste des chambres occupées"),
    Gtk.Button(label="Liste des chambres reservées"),
    Gtk.Button(label="Modifier classe d'une chambre"),
    Gtk.Button(label="Chambres: Economiques"),
    Gtk.Button(label="Chambres: Standing"),
    Gtk.Button(label="Chambres: Affaires"),
    Gtk.Button(label="Retour"),
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    ChambresBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)
