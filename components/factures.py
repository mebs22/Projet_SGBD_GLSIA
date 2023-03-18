from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING


# Creating container
FacturesBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
BUTTONS = [
    ListFacturesBtn,
    LisTodayFacturesBtn,
    BackBtn
] = [
    Gtk.Button(label="Liste des factures"),
    Gtk.Button(label="Les factures d'aujourd'hui"),
    Gtk.Button(label="Retour"),
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    FacturesBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)
