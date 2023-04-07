import os
from drawer import Drawer 

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class UI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.dirname(__file__) + "/glade/main.glade")

        self.win = self.builder.get_object("window")
        self.mainDrawingArea = self.builder.get_object("mainDrawingArea")

        self.drawer = Drawer(self.mainDrawingArea)

    def run(self):
        self.win.connect("destroy", Gtk.main_quit)

        self.win.show_all()
        Gtk.main()

if __name__ == "__main__":
    ui = UI()
    ui.run()