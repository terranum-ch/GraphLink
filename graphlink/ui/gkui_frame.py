#!/urs/bin/python

import wx
import wx.aui
# from ..core.gk_node import GKNode (this code works for importing)

###########################################################################
# Class GKUIFrame
###########################################################################


class GKUIFrame (wx.Frame):
    """GraphLink main window"""
    def __init__(self, parent=None):
        wx.Frame.__init__(
            self, parent=parent, id=wx.ID_ANY, title=u"GraphLink",
            pos=wx.DefaultPosition, size=wx.Size(500, 300),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.m_panel_node = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.m_panel_node, wx.aui.AuiPaneInfo() .Left() .Caption( u"Nodes" ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 200,36 ) ).Row( 1 ).MinSize( wx.Size( 200,200 ) ).Layer( 0 ) )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_search_node_ctrl = wx.SearchCtrl( self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_search_node_ctrl.ShowSearchButton( True )
        self.m_search_node_ctrl.ShowCancelButton( True )
        bSizer2.Add( self.m_search_node_ctrl, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_list_node_ctrl = wx.ListCtrl( self.m_panel_node, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), wx.LC_LIST|wx.LC_NO_HEADER )
        bSizer2.Add( self.m_list_node_ctrl, 1, wx.EXPAND, 5 )


        self.m_panel_node.SetSizer( bSizer2 )
        self.m_panel_node.Layout()
        bSizer2.Fit( self.m_panel_node )
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.m_panel2, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( True ).BottomDockable( False ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ) )


        self.m_mgr.Update()
        self.Centre( wx.BOTH )

    def __del__(self):
        self.m_mgr.UnInit()


