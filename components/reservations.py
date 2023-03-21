from gtk_imports import Gtk
from components.constants import *
# from mainFunctions import insertComponentName
from mainFunctions import *
from components.constants import API_URL
import requests
import json

def generateReservations(stack):

    # Creating container
    ReservationsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("RESERVATIONS") )
    ComponentName.set_size_request(-1, 200)

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
    ReservationsBox.pack_start(ComponentName, True, True, DEFAULT_BOX_SPACING)
    for BTN in BUTTONS:
        ReservationsBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)

    
    return ReservationsBox

def seeReservationData():
    response = requests.get(f"{API_URL}/posts", headers=REQUEST_HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def generateVoirReservations(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("LISTE DES RESERVATIONS") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")
    
    # Tree view creation
    tree_view = Gtk.TreeView()
    ScrollWindow = Gtk.ScrolledWindow()
    ScrollWindow.add(tree_view)
    ScrollWindow.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    ScrollWindow.set_size_request(-1, 400)
    column_names = ["Chambre", "Date entree", "Date sortie"]

    try:
        fetched_data = seeReservationData()
    except:
        print("Erreur de chargement des donees de reservation")
        fetched_data = []

    print(fetched_data)

    for i, col_title in enumerate(column_names):
        render = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(col_title, render, text=i)
        tree_view.append_column(column)

    liststore = Gtk.ListStore(str, str, str)

    for item in fetched_data:
        liststore.append([str(item["id"]), item["title"], item["body"][0]])
    
    tree_view.set_model(liststore)


    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))


    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(ScrollWindow, False, True, 0)
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
    # BackBtn = Gtk.Button(label="Retour")
    Form = createAddForm(stack)

    # Binding callbacks
    # BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))

    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(Form, True, True, 0)
    # Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)


    return Container


def generateSupprimerReservation(stack):
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("SUPPRIMER UNE RESERVATION") )
    ComponentName.set_size_request(-1, 200)

    # Creating elements
    # BackBtn = Gtk.Button(label="Retour")
    Form = createDelteForm(stack)

    # Binding callbacks
    # BackBtn.connect("clicked", lambda y: changePage(stack, RESERVATIONS))


    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(Form, True, True, 0)
    # Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)


    return Container



# FUNCTIONS HERE!
def createAddForm(stack):
    # Create a box to hold the form elements
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

    # Create a fieldset
    fieldset = Gtk.Frame()
    box.pack_start(fieldset, False, False, 0)

    # Create a grid to hold the form elements
    grid = Gtk.Grid(column_spacing=10, row_spacing=10)
    fieldset.add(grid)

    # Create the form inputs with placeholders
    prenom = Gtk.Entry(placeholder_text="Prenom")
    prenom.set_hexpand(True)
    nom = Gtk.Entry(placeholder_text="Nom")
    nom.set_hexpand(True)
    numero = Gtk.Entry(placeholder_text="Numéro")
    numero.set_hexpand(True)
    chambre = Gtk.Entry(placeholder_text="Chambre")
    chambre.set_hexpand(True)
    nuite = Gtk.Entry(placeholder_text="Nuité")
    nuite.set_hexpand(True)

    # Add the inputs to the grid
    grid.attach(prenom, 0, 0, 1, 1)
    grid.attach(nom, 0, 1, 1, 1)
    grid.attach(numero, 0, 2, 1, 1)
    grid.attach(chambre, 0, 3, 1, 1)
    grid.attach(nuite, 0, 4, 1, 1)

    # Create the submit and cancel buttons
    submit_button = Gtk.Button.new_with_label("Enregistrer")
    submit_button.get_style_context().add_class("suggested-action")
    submit_button.get_style_context().add_class("text-white")
    cancel_button = Gtk.Button.new_with_label("Annuler")
    cancel_button.get_style_context().add_class("destructive-action")
    cancel_button.get_style_context().add_class("text-white")

    # Binding functions
    submit_button.connect("clicked", lambda y: getAddFormData(box, stack))
    cancel_button.connect("clicked", lambda y: changePage(stack, RESERVATIONS))

    # Add the buttons to the box
    box.pack_start(submit_button, False, False, 0)
    box.pack_start(cancel_button, False, False, 0)

    return box

def getAddFormData(form, stack):
    prenom = form.get_children()[0].get_children()[0].get_children()[0]
    nom = form.get_children()[0].get_children()[0].get_children()[1]
    numero = form.get_children()[0].get_children()[0].get_children()[2]
    chambre = form.get_children()[0].get_children()[0].get_children()[3]
    nuite = form.get_children()[0].get_children()[0].get_children()[4]

    data = {
        "prenom": prenom.get_text(),
        "nom": nom.get_text(),
        "numero": numero.get_text(),
        "chambre": chambre.get_text(),
        "nuite": nuite.get_text()
    }

    if(data["prenom"] == '' or data["nom"] == '' or data["numero"] == '' or data["chambre"] == '' or data["nuite"] == ''):
        open_dialog("Un champ est vide")
        return None

    print(data)
    json_data = json.dumps(data)

    # API call
    response = requests.post(f"{API_URL}/{RESERVATION}", headers=REQUEST_HEADERS, data=json_data)
    if response.status_code == 200:
        open_dialog("Reservation enregistree")
        print("Reservation enregistree")
        changePage(stack, RESERVATIONS)
    else:
        open_dialog("Erreur lors de l'enregistrement de la reservation")
        print("Erreur lors de l'enregistrement de la reservation")
        changePage(stack, RESERVATIONS)

    # return json_data

def createDelteForm(stack):
    # Create a box to hold the form elements
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

    # Create a fieldset
    fieldset = Gtk.Frame()
    box.pack_start(fieldset, False, False, 0)

    # Create a grid to hold the form elements
    grid = Gtk.Grid(column_spacing=10, row_spacing=10)
    fieldset.add(grid)

    # Create the form inputs with placeholders
    client = Gtk.Entry(placeholder_text="Numéro client")
    client.set_hexpand(True)
    reservation = Gtk.Entry(placeholder_text="Numéro réservation")
    reservation.set_hexpand(True)

    # Add the inputs to the grid
    grid.attach(client, 0, 0, 1, 1)
    grid.attach(reservation, 0, 1, 1, 1)

    # Create the submit and cancel buttons
    submit_button = Gtk.Button.new_with_label("Supprimer")
    submit_button.get_style_context().add_class("suggested-action")
    submit_button.get_style_context().add_class("text-white")
    cancel_button = Gtk.Button.new_with_label("Annuler")
    cancel_button.get_style_context().add_class("destructive-action")
    cancel_button.get_style_context().add_class("text-white")
    
    # Binding functions
    submit_button.connect("clicked", lambda y: getDelFormData(box, stack))
    cancel_button.connect("clicked", lambda y: changePage(stack, RESERVATIONS))

    # Add the buttons to the box
    box.pack_start(submit_button, False, False, 0)
    box.pack_start(cancel_button, False, False, 0)

    return box

def getDelFormData(form, stack):
    client = form.get_children()[0].get_children()[0].get_children()[0]
    reservation = form.get_children()[0].get_children()[0].get_children()[1]

    data = {
        "client": client.get_text(),
        "reservation": reservation.get_text(),
    }

    if(data["client"] == '' or data["reservation"]):
        open_dialog("Un champ est vide")
        return None

    json_data = json.dumps(data)
    # print(json_data)

    # API call
    response = requests.delete(f"{API_URL}/{RESERVATION}", headers=REQUEST_HEADERS, data=json_data)
    if response.status_code == 200:
        open_dialog("Reservation enregistree")
        print("Reservation enregistree")
        changePage(stack, RESERVATIONS)
    else:
        open_dialog("Erreur lors de l'enregistrement de la reservation")
        print("Erreur lors de l'enregistrement de la reservation")
        changePage(stack, RESERVATIONS)

    # return json_data





def open_dialog(message):
    # create the dialog
    dialog = Gtk.MessageDialog(
        parent=None,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text=message
    )

    # run the dialog and wait for a response
    response = dialog.run()

    # close the dialog
    dialog.destroy()