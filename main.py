from gtk_imports import Gtk
from components.mainMenu import MenuBox

PROGRAM_NAME = "Hotel Manager"

Win = Gtk.Window(title=PROGRAM_NAME)
Win.connect("destroy", Gtk.main_quit)


# Geneating grid
AppGrid = Gtk.Grid()

# Wrapping for alignment
Aligner = Gtk.Alignment(halign=Gtk.Align.CENTER, valign=Gtk.Align.START)
Aligner.add(AppGrid)

# Adding elements to gridAppName
AppGrid.attach(MenuBox, 0, 1, 1, 1)

# Adding elements to main window
Win.add(Aligner)

# Rendering
Win.maximize()
Win.show_all()
Gtk.main()