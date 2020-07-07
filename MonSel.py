import gi
import subprocess
import re
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def onOnlyInternal(self, button):
        cmd = subprocess.Popen(['xrandr','--output',device[-1],'--off','--output',device[0],'--auto'], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onOnlyExternal(self, button):
        cmd = subprocess.Popen(['xrandr','--output',device[0],'--off','--output',device[-1],'--auto'], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onMirrored(self, button):
        cmd = subprocess.Popen(['xrandr','--output',device[0],'--auto','--output',device[-1],'--auto','--same-as',device[0]], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onExtended(self, button):
        cmd = subprocess.Popen(['xrandr','--output',device[0],'--auto','--output',device[-1],'--auto','--right-of',device[0]], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
 
xrandr = subprocess.Popen(['xrandr'], stdout=subprocess.PIPE)
out, err = xrandr.communicate()
out = out.decode("utf-8")
device = []
for line in out.split('\n'):
    if(re.findall('\\bconnected\\b', line)):
        temp = line.split()
        device.append(temp[0])
builder = Gtk.Builder()
builder.add_from_file("MonSel_GUI.glade")
builder.connect_signals(Handler())
window = builder.get_object("MonSel")
internalDispName = builder.get_object("internalDispName")
internalDispName.set_text("Internal: "+device[0])
externalDispName = builder.get_object("externalDispName")

if(len(device) == 1):
    externalDispName.set_text("External: Not Connected")
else:
    externalDispName.set_text("External: "+device[1])
window.show_all()

Gtk.main()
