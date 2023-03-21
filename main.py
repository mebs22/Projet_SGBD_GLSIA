from gtk_imports import Gtk
from components.constants import *
from components.mainMenu import generateMenu
from components.chambres import generateChambres, generateChambresLibres, generateChambresOccupees
from components.reservations import generateReservations, generateAjouterReservation, generateVoirReservations, generateSupprimerReservation
from components.factures import generateFactures
from components.stats import generateStats
from mainFunctions import *

PROGRAM_NAME = "Hotel Manager"

Win = Gtk.Window(title=PROGRAM_NAME)
Win.connect("destroy", Gtk.main_quit)

# Creating stack
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

# Creating pages
MainMenu = generateMenu(stack)

Chambres = generateChambres(stack)
ChambresLibres = generateChambresLibres(stack)
ChambresOccupees = generateChambresOccupees(stack)

Reservations = generateReservations(stack)
VoirReservations = generateVoirReservations(stack)
AjouterReservation = generateAjouterReservation(stack)
SupprimerReservation = generateSupprimerReservation(stack)

Factures = generateFactures(stack)

Stats = generateStats(stack)

# Adding pages to stack
stack.add_titled(MainMenu, MAIN, "Menu Principal")

stack.add_titled(Chambres, CHAMBRES, "Liste des chambres")
stack.add_titled(ChambresLibres, CHAMBRE_LIBRE, "Chambres Libres")
stack.add_titled(ChambresOccupees, CHAMBRE_OCCUPEE, "ChambresOccupees")

stack.add_titled(Reservations, RESERVATIONS, "Reservations")
stack.add_titled(VoirReservations, VOIR_RESERVATIONS, "Voir Reservations")
stack.add_titled(AjouterReservation, AJOUTER_RESERVATION, "Ajouter Reservation")
stack.add_titled(SupprimerReservation, SUPPRIMER_RESERVATION, "Supprimer Reservation")

stack.add_titled(Factures, FACTURES, "Factures")

stack.add_titled(Stats, STATS, "Stats")


# Rendering
Win.add(stack)
Win.maximize()
Win.show_all()

Gtk.main()