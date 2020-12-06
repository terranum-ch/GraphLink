import wx
import os
from graphlink.ui.gkui_frame import GKUIFrame

# copy Graphviz exe in lib/bin directory for a no-install build.
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib", "bin"))
if os.path.exists(lib_path):
    os.environ["PATH"] += os.pathsep + lib_path
    print (os.environ["PATH"])


##########################################################
#  MAIN APP CLASS
##########################################################


class GKUIApp(wx.App):
    """
    GraphLink application class
    initialize the GKUIFrame class and the main loop
    """
    def OnInit(self):
        dlg = GKUIFrame()
        dlg.Show(True)
        self.SetTopWindow(dlg)
        return True


app = GKUIApp()
app.MainLoop()
