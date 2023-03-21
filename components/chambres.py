from gtk_imports import Gtk
from components.constants import *
from mainFunctions import insertComponentName
from mainFunctions import *
import requests

def seeChambresData():
    response = requests.get(f"{API_URL}/posts", headers=REQUEST_HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def generateChambres(stack):
    # Creating container
    ChambresBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("LISTE DES CHAMBRES") )
    ComponentName.set_size_request(-1, 200)


    # Creating Buttons
    BUTTONS = [
        ListFreeRoomsBtn,
        ListOccupiedRoomsBtn,
        BackBtn
    ] = [
        Gtk.Button(label="Chambres libres"),
        Gtk.Button(label="Chambres occupées"),
        Gtk.Button(label="Retour"),
    ]

    # Binding callbacks
    BUTTONS[0].connect("clicked", lambda y: changePage(stack, CHAMBRE_LIBRE))
    BUTTONS[1].connect("clicked", lambda y: changePage(stack, CHAMBRE_OCCUPEE))
    BUTTONS[2].connect("clicked", lambda y: goBack(stack))

    # Stacking elements
    ChambresBox.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    for BTN in BUTTONS:
        ChambresBox.pack_start(BTN, True, True, DEFAULT_BUTTON_PADDING)

    return ChambresBox

def generateChambresLibres(stack): 
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("CHAMBRES LIBRES") )
    ComponentName.set_size_request(-1, 200)

    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, CHAMBRES))


    # Tree view creation
    tree_view = Gtk.TreeView()
    ScrollWindow = Gtk.ScrolledWindow()
    ScrollWindow.add(tree_view)
    ScrollWindow.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    ScrollWindow.set_size_request(-1, 400)
    column_names = ["Numero", "Classe"]

    try:
        fetched_data = seeChambresData() 
    except:
        print("Erreur de chargement des donees de chambres Libres")
        fetched_data = []


    for i, col_title in enumerate(column_names):
        render = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(col_title, render, text=i)
        tree_view.append_column(column)

    liststore = Gtk.ListStore(str, str)

    for item in fetched_data:
        liststore.append([str(item["id"]), item["title"]])
    
    tree_view.set_model(liststore)

    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(ScrollWindow, False, True, 0)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)

    return Container


def generateChambresOccupees(stack): 
    # Creating container
    Container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=DEFAULT_BOX_SPACING)

    # Creating elements
    BackBtn = Gtk.Button(label="Retour")

    # Tree view creation
    tree_view = Gtk.TreeView()
    ScrollWindow = Gtk.ScrolledWindow()
    ScrollWindow.add(tree_view)
    ScrollWindow.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    ScrollWindow.set_size_request(-1, 400)
    column_names = ["Numero", "Classe"]

    try:
        fetched_data = seeChambresData() 
    except:
        print("Erreur de chargement des donees de chambres occupees")
        fetched_data = []


    for i, col_title in enumerate(column_names):
        render = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(col_title, render, text=i)
        tree_view.append_column(column)

    liststore = Gtk.ListStore(str, str)

    for item in fetched_data:
        liststore.append([str(item["id"]), item["title"]])
    
    tree_view.set_model(liststore)


    # Generating Component name
    ComponentName = Gtk.Label()
    ComponentName.set_markup( insertComponentName("CHAMBRES OCCUPEES") )
    ComponentName.set_size_request(-1, 200)

    
    # Binding callbacks
    BackBtn.connect("clicked", lambda y: changePage(stack, CHAMBRES))



    # Stacking elements
    Container.pack_start(ComponentName, True, True, DEFAULT_BUTTON_PADDING)
    Container.pack_start(ScrollWindow, False, True, 0)
    Container.pack_start(BackBtn, True, True, DEFAULT_BUTTON_PADDING)

    return Container
