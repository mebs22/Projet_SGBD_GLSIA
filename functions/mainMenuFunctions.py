from gtk_imports import Gtk
from components.constants import *
from components.stats import StatsBox
from components.clients import ClientsBox
from components.factures import FacturesBox
from components.chambres import ChambresBox
from components.gestionHotel import GesHotelBox
from components.reservations import ReservationsBox

COMPONENT_LIST = {
    GESTION_HOTEL : GesHotelBox,
    CHAMBRES : ChambresBox,
    CLIENTS : ClientsBox,
    RESERVATIONS : ReservationsBox,
    FACTURES : FacturesBox,
    STATS : StatsBox,
}

HELP_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis massa et porttitor molestie. Nunc convallis metus et auctor pulvinar. Nam elementum nibh sit amet consequat facilisis. Sed dui purus, auctor sed lectus nec, sodales porttitor dui. Maecenas nec nibh iaculis, posuere ex in, tristique metus. Donec ac venenatis ex. Aliquam auctor sem eu tellus auctor sodales. Praesent finibus risus auctor nisl feugiat, accumsan volutpat purus laoreet. Maecenas dolor lorem, luctus ut ante ac, varius cursus ante. Ut in fringilla mauris, a convallis lacus. Mauris velit quam, egestas et lorem vel, pharetra consequat elit. Nullam eu neque lorem. Nam vulputate, lacus nec maximus tristique, urna lectus varius nulla, a condimentum dui felis ut metus. Quisque ullamcorper erat diam, nec accumsan diam maximus non.

Aliquam et mi finibus, gravida libero dignissim, pretium nunc. In congue, velit nec venenatis iaculis, diam neque laoreet ligula, ut laoreet erat lorem a nisl. Donec feugiat commodo laoreet. Morbi eu urna sed ipsum sodales ultricies. Sed ut tellus et lorem tempor feugiat id vitae mauris. Cras convallis dolor vestibulum tortor commodo porttitor vehicula et elit. Fusce porta sapien eu metus facilisis tempus. Donec non lectus vitae dolor pellentesque rutrum a in est. In aliquam malesuada felis, eget ullamcorper nisi elementum ut. Etiam nisi dui, hendrerit efficitur ultricies non, ultricies nec tortor. Maecenas lobortis ultrices odio, vel bibendum ligula vestibulum lacinia. Proin volutpat diam in scelerisque fringilla. Ut tincidunt nibh in sem mollis, sed pulvinar tortor sodales. Nunc massa tellus, porta id velit in, iaculis egestas eros. Etiam pharetra nibh elementum metus sollicitudin vehicula at ac dui. Donec dictum, velit cursus ultricies semper, est orci dapibus metus, sit amet ultricies sapien tortor sit amet elit.zz"""

def loadComponent(element, boxType):
    # Get parent
    elementRoot = element.get_parent()

    # Remove the current element
    elementRoot.remove(element)

    # Attach new component and "re-render"
    elementRoot.attach(COMPONENT_LIST[boxType], 0, 1, 1, 1)
    elementRoot.show_all()

def showHelp(widget):
    dialog = Gtk.MessageDialog(parent=None, flags=0, message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK, text=HELP_TEXT)
    dialog.format_secondary_text("This is some help text.")
    dialog.run()
    dialog.destroy()