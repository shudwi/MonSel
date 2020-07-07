import gi
import subprocess
import re
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MonSel:
    device = []
    def __init__(self):
        xrandr = subprocess.Popen(['xrandr'], stdout=subprocess.PIPE)
        out, err = xrandr.communicate()
        out = out.decode("utf-8")
        for line in out.split('\n'):
            if(re.findall('\\bconnected\\b', line)):
                temp = line.split()
                MonSel.device.append(temp[0])
        MonSel.Main()
        
    def Main():
        builder = Gtk.Builder()
        builder.add_from_file("MonSel_GUI.glade")
        builder.connect_signals(Handler())
        window = builder.get_object("MonSel")
        internalDispName = builder.get_object("internalDispName")
        internalDispName.set_text("Internal: "+MonSel.device[0])
        externalDispName = builder.get_object("externalDispName")
        if(len(MonSel.device) == 1):
            externalDispName.set_text("External: Not Connected")
        else:
            externalDispName.set_text("External: "+MonSel.device[1])
        window.show_all()
        Gtk.main()

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def onOnlyInternal(self, button):
        cmd = subprocess.Popen(['xrandr','--output',MonSel.device[-1],'--off','--output',MonSel.device[0],'--auto'], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onOnlyExternal(self, button):
        cmd = subprocess.Popen(['xrandr','--output',MonSel.device[0],'--off','--output',MonSel.device[-1],'--auto'], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onMirrored(self, button):
        cmd = subprocess.Popen(['xrandr','--output',MonSel.device[0],'--auto','--output',MonSel.device[-1],'--auto','--same-as',MonSel.device[0]], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
    def onExtended(self, button):
        cmd = subprocess.Popen(['xrandr','--output',MonSel.device[0],'--auto','--output',MonSel.device[-1],'--auto','--right-of',MonSel.device[0]], stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
 

if __name__ == "__main__":MonSel()
