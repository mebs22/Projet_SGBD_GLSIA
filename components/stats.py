from gtk_imports import Gtk
from components.constants import DEFAULT_BOX_SPACING, DEFAULT_BUTTON_PADDING


# Creating container
StatsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

# Creating Buttons
BUTTONS = [
    MonthlyBtn,
    SemNYearlyBtn,
    BackBtn
] = [
    Gtk.Button(label="Mensuel"),
    Gtk.Button(label="Semestre & Annuel"),
    Gtk.Button(label="Retour"),
]

# Binding callbacks

# Stacking elements
for BTN in BUTTONS:
    StatsBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)
