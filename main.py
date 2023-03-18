from gtk_imports import Gtk
from components.mainMenu import MenuBox
from components.gestionHotel import GesHotelBox
from mainFunctions import insertComponentName

PROGRAM_NAME = "Hotel Manager"

Win = Gtk.Window(title=PROGRAM_NAME)
Win.connect("destroy", Gtk.main_quit)

# Geneating grid
AppGrid = Gtk.Grid()

# Generating the global app name
AppName = Gtk.Label()
AppName.set_markup( insertComponentName("MENU PRINCIPAL") )
AppName.set_size_request(-1, 200)

# Wrapping for alignment
Aligner = Gtk.Alignment(halign=Gtk.Align.CENTER, valign=Gtk.Align.START)
Aligner.add(AppGrid)

# Adding elements to grid
AppGrid.attach(AppName, 0, 0, 1, 1)
AppGrid.attach(MenuBox, 0, 1, 1, 1)


# Adding elements to main window
Win.add(Aligner)

# Rendering
Win.maximize()
Win.show_all()
Gtk.main()