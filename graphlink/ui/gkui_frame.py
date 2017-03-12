#!/urs/bin/python
import os
import sys
import platform
import wx
import wx.aui
import wx.html

from .gkui_node_manager import GKUINodeManager


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "art",  relative_path)
    return os.path.join(os.path.dirname(__file__), "..", "art", relative_path)

###########################################################################
# Class GKUIFrame
###########################################################################


class GKUIFrame (wx.Frame):
    """GraphLink main window"""
    def __init__(self, parent=None):
        wx.Frame.__init__(
            self, parent=parent, id=wx.ID_ANY, title=u"GraphLink",
            pos=wx.DefaultPosition, size=wx.Size(800, 500),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # UI
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.m_panel_node = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_node, wx.aui.AuiPaneInfo() .Left() .Caption(u"Nodes").CloseButton(False).Dock().Resizable().FloatingSize(wx.Size(200,36) ).Row(1).MinSize(wx.Size(200,200) ).Layer(0) )

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_search_node_ctrl = wx.SearchCtrl(self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_search_node_ctrl.ShowSearchButton(True)
        self.m_search_node_ctrl.ShowCancelButton(True)
        bSizer2.Add(self.m_search_node_ctrl, 0, wx.ALL|wx.EXPAND, 5)

        self.m_list_node_ctrl = wx.ListCtrl(self.m_panel_node, wx.ID_ANY, wx.DefaultPosition, wx.Size(250,-1), wx.LC_LIST)
        bSizer2.Add(self.m_list_node_ctrl, 1, wx.EXPAND, 5)


        self.m_panel_node.SetSizer(bSizer2)
        self.m_panel_node.Layout()
        bSizer2.Fit(self.m_panel_node)
        self.m_panel_main = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_main, wx.aui.AuiPaneInfo() .Center() .CaptionVisible(False).CloseButton(False).PaneBorder(False).Movable(False).Dock().Resizable().FloatingSize(wx.DefaultSize).DockFixed(True).BottomDockable(False).TopDockable(False).LeftDockable(False).RightDockable(False).Floatable(False).CentrePane())

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_htmlWin1 = wx.html.HtmlWindow(self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO)
        bSizer3.Add(self.m_htmlWin1, 1, wx.EXPAND, 5)


        self.m_panel_main.SetSizer(bSizer3)
        self.m_panel_main.Layout()
        bSizer3.Fit(self.m_panel_main)
        self.m_panel_link = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_link, wx.aui.AuiPaneInfo() .Right() .Caption(u"Links").CloseButton(False).Dock().Resizable().FloatingSize(wx.Size(400,250) ).Row(1).Position(1).MinSize(wx.Size(200,250) ))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_search_link_ctrl = wx.SearchCtrl(self.m_panel_link, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_search_link_ctrl.ShowSearchButton(True)
        self.m_search_link_ctrl.ShowCancelButton(True)
        bSizer4.Add(self.m_search_link_ctrl, 0, wx.ALL|wx.EXPAND, 5)

        self.m_listCtrl2 = wx.ListCtrl(self.m_panel_link, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST)
        bSizer4.Add(self.m_listCtrl2, 1, wx.EXPAND, 5)


        self.m_panel_link.SetSizer(bSizer4)
        self.m_panel_link.Layout()
        bSizer4.Fit(self.m_panel_link)

        # create the menubar / toolbar / statusbar 
        self._create_menubar()
        self._create_toolbar()
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

        # Node Manager
        self.m_node_manager = GKUINodeManager(self, self.m_list_node_ctrl)

        # Connect Events
        # Menu event
        self.Bind(wx.EVT_MENU, self.OnNodeSetPath, id=self.m_menu_node_path.GetId())
        self.Bind(wx.EVT_MENU, self.OnNodeAdd, id=self.m_menu_node_add.GetId())
        self.Bind(wx.EVT_MENU, self.OnNodeEdit, id=self.m_menu_node_edit.GetId())
        
        # node list event
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnNodeEdit, id=self.m_list_node_ctrl.GetId())

        # ui event
        self.Bind(wx.EVT_UPDATE_UI, self.OnNoNodeSelected, id=self.m_menu_node_edit.GetId())
    
    def _create_menubar(self):
        self.m_menubar = wx.MenuBar(0)

        # node menu
        self.m_menu_nodes = wx.Menu()
        self.m_menu_node_path = wx.MenuItem(
            self.m_menu_nodes, wx.ID_ANY,
            u"Set path...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_nodes.Append(self.m_menu_node_path)
        self.m_menu_nodes.AppendSeparator()
        self.m_menu_node_add = wx.MenuItem(
            self.m_menu_nodes, wx.ID_ANY,
            u"Add...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_nodes.Append(self.m_menu_node_add)
        self.m_menu_node_edit = wx.MenuItem(
            self.m_menu_nodes, wx.ID_ANY,
            u"Edit...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_nodes.Append(self.m_menu_node_edit)
        self.m_menu_node_remove = wx.MenuItem(
            self.m_menu_nodes, wx.ID_ANY,
            u"Remove", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_nodes.Append(self.m_menu_node_remove)
        self.m_menu_nodes.AppendSeparator()
        self.m_menu_node_reload = wx.MenuItem(
            self.m_menu_nodes, wx.ID_ANY,
            u"Reload", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_nodes.Append(self.m_menu_node_reload)
        self.m_menubar.Append(self.m_menu_nodes, u"Nodes")

        self.SetMenuBar(self.m_menubar)

    def _create_toolbar(self,):
       # no text for windows 
        style = wx.TB_DEFAULT_STYLE | wx.TB_TEXT
        if "Windows" in platform.system(): 
            style = wx.TB_DEFAULT_STYLE

        self.m_toolBar = self.CreateToolBar(style)
        self.m_toolBar.SetToolBitmapSize(wx.Size(32, 32))
        self.m_tool_node_import = self.m_toolBar.AddTool(
            self.m_menu_node_path.GetId(),
            u"Import nodes",
            wx.Bitmap(resource_path("node_import.png")),
            wx.NullBitmap,
            wx.ITEM_NORMAL,
            u"Import nodes",
            wx.EmptyString,
            None) 
        self.m_toolBar.Realize()

    def __del__(self):
        self.m_mgr.UnInit()

    def OnNodeSetPath(self, event):
        wx.LogMessage("Node import")
        event.Skip()

    def OnNodeAdd(self, event):
        self.m_node_manager.add_node_dialog()

    def OnNodeEdit(self, event):
        self.m_node_manager.edit_node_dialog()

    def OnNoNodeSelected(self, event):
        if self.m_list_node_ctrl.GetFirstSelected() == -1:  # no selection
            event.Enable(False)
        else:
            event.Enable(True)
