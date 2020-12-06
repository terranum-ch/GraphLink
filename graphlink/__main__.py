import wx
from graphlink.ui.gkui_frame import GKUIFrame


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
