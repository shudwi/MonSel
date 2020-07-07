import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def onOnlyInternal(self, button):
        print("only Internal")
    def onOnlyExternal(self, button):
        print("Only External")
    def onMirrored(self, button):
        print("Mirrored")
    def onExtended(self, button):
        print("Extended")

builder = Gtk.Builder()
builder.add_from_file("MonSel_GUI.glade")
builder.connect_signals(Handler())
window = builder.get_object("MonSel")
window.show_all()

Gtk.main()
