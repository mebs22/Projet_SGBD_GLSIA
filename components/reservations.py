from gtk_imports import Gtk
from components.constants import *
from mainFunctions import insertComponentName
from mainFunctions import *

def generateReservations(stack):

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
        Gtk.Button(label="Supprimer une reservation"),
        Gtk.Button(label="Retour"),
    ]

    # Binding callbacks
    BUTTONS[0].connect("clicked", lambda y: changePage(stack, VOIR_RESERVATIONS))
    BUTTONS[1].connect("clicked", lambda y: changePage(stack, AJOUTER_RESERVATION))
    BUTTONS[2].connect("clicked", lambda y: changePage(stack, SUPPRIMER_RESERVATION))
    BUTTONS[3].connect("clicked", lambda y: goBack(stack))

    # Stacking elements
    for BTN in BUTTONS:
        ReservationsBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)

    
    return ReservationsBox

def generateVoirReservations(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("LISTE DES RESERVATIONS") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))


    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)



    return Container


def generateAjouterReservation(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("AJOUTER UNE RESERVATION") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))

    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)


    return Container


def generateSupprimerReservation(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("SUPPRIMER UNE RESERVATION") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))


    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)


    return Container
