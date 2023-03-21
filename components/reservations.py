from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING


# Creating container
ReservationsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
BUTTONS = [
    ListReservationsBtn,
    AddReservationsBtn,
    CancelReservationsBtn,
    BackBtn
] = [
    Gtk.Button(label="Voir les reservations"),
    Gtk.Button(label="Ajouter une reservation"),
    Gtk.Button(label="Annuler une reservation"),
    Gtk.Button(label="Retour"),
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    ReservationsBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)
