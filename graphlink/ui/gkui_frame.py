#!/urs/bin/python

import os
import platform
import sys

import wx
import wx.aui
import wx.html

from .gkui_graphic_manager import GKUIGraphicManager
from .gkui_node_manager import GKUINodeManager


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "art", relative_path)
    return os.path.join(os.path.dirname(__file__), "..", "art", relative_path)


###########################################################################
# Class GKUIFrame
###########################################################################


class GKUIFrame(wx.Frame):
    """GraphLink main window"""

    def __init__(self, parent=None):
        wx.Frame.__init__(
            self, parent=parent, id=wx.ID_ANY, title=u"GraphLink",
            pos=wx.DefaultPosition, size=wx.Size(800, 500),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # UI
        self._create_controls()

        # Init Managers
        self.m_node_manager = GKUINodeManager(self, self.m_list_node_ctrl)
        self.m_graphic_manager = GKUIGraphicManager(
            parentframe=self, linklist=self.m_list_link_ctrl,
            display=self.m_html_win, nodemanager=self.m_node_manager)

        # Connect Events
        # Menu event
        self.Bind(wx.EVT_MENU, self.OnNodeAdd, id=self.m_menu_node_add.GetId())
        self.Bind(wx.EVT_MENU, self.OnNodeEdit, id=self.m_menu_node_edit.GetId())
        self.Bind(wx.EVT_MENU, self.OnLinkAdd, id=self.m_menu_link_add.GetId())
        self.Bind(wx.EVT_MENU, self.OnGraphGenerate, id=self.m_menu_graph_generate.GetId())

        # node list event
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnNodeEdit, id=self.m_list_node_ctrl.GetId())

        # ui event
        self.Bind(wx.EVT_UPDATE_UI, self.OnNoNodeSelected, id=self.m_menu_node_edit.GetId())
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateStatusBar, id=self.m_statusBar.GetId())

        # destroy event
        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)

    def OnDestroy(self, event):
        """Unit the AUI Manager, otherwise It will crash
           This function is Always called when Windows is Destroyed"""
        self.m_mgr.UnInit()
        event.Skip()

    def _create_menubar(self):
        self.m_menubar = wx.MenuBar(0)

        # file menu
        self.m_menu_file = wx.Menu()
        self.m_menu_file_new = wx.MenuItem(
            self.m_menu_file, wx.ID_NEW,
            u"New", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_file.Append(self.m_menu_file_new)
        self.m_menu_file_open = wx.MenuItem(
            self.m_menu_file, wx.ID_OPEN,
            u"Open...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_file.Append(self.m_menu_file_open)
        self.m_menu_file.AppendSeparator()
        self.m_menu_file_exit = wx.MenuItem(
            self.m_menu_file, wx.ID_EXIT,
            u"Exit...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_file.Append(self.m_menu_file_exit)
        self.m_menubar.Append(self.m_menu_file, u"File")

        # node menu
        self.m_menu_nodes = wx.Menu()
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

        # links menu
        self.m_menu_links = wx.Menu()
        self.m_menu_link_add = wx.MenuItem(
            self.m_menu_links, wx.ID_ANY,
            u"Add...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_links.Append(self.m_menu_link_add)

        self.m_menu_link_edit = wx.MenuItem(
            self.m_menu_links, wx.ID_ANY,
            u"Edit...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_links.Append(self.m_menu_link_edit)

        self.m_menu_link_remove = wx.MenuItem(
            self.m_menu_links, wx.ID_ANY,
            u"Remove", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_links.Append(self.m_menu_link_remove)

        self.m_menubar.Append(self.m_menu_links, u"Links")

        # graphic menu
        self.m_menu_graph = wx.Menu()
        self.m_menu_graph_generate = wx.MenuItem(
            self.m_menu_graph, wx.ID_ANY, u"Refresh",
            wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_graph.Append(self.m_menu_graph_generate)

        self.m_menubar.Append(self.m_menu_graph, u"Graphic")

        self.SetMenuBar(self.m_menubar)

    def _create_toolbar(self, ):
        # no text for windows
        style = wx.TB_DEFAULT_STYLE | wx.TB_TEXT
        if "Windows" in platform.system():
            style = wx.TB_DEFAULT_STYLE

        self.m_toolBar = self.CreateToolBar(style)
        self.m_toolBar.SetToolBitmapSize(wx.Size(32, 32))
        self.m_tool_file_open = self.m_toolBar.AddTool(
            self.m_menu_file_open.GetId(),
            u"Open...",
            wx.Bitmap(resource_path("file_open.png")),
            wx.NullBitmap,
            wx.ITEM_NORMAL,
            u"Open...",
            wx.EmptyString,
            None)
        self.m_tool_node_add = self.m_toolBar.AddTool(
            self.m_menu_node_add.GetId(),
            u"Add node...",
            wx.Bitmap(resource_path("node.png")),
            wx.NullBitmap,
            wx.ITEM_NORMAL,
            u"Add node...",
            wx.EmptyString,
            None)
        self.m_tool_link_add = self.m_toolBar.AddTool(
            self.m_menu_link_add.GetId(),
            u"Add link...",
            wx.Bitmap(resource_path("link.png")),
            wx.NullBitmap,
            wx.ITEM_NORMAL,
            u"Add link...",
            wx.EmptyString,
            None)
        self.m_tool_graph_reload = self.m_toolBar.AddTool(
            self.m_menu_graph_generate.GetId(),
            u"Refresh...",
            wx.Bitmap(resource_path("graph_reload.png")),
            wx.NullBitmap,
            wx.ITEM_NORMAL,
            u"Refresh...",
            wx.EmptyString,
            None)
        self.m_toolBar.Realize()

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

    def OnUpdateStatusBar(self, event):
        self.m_statusBar.SetStatusText(
            "Nodes: {}".format(self.m_node_manager.get_node_count()))

    def OnLinkAdd(self, event):
        self.m_graphic_manager.add_link_dialog()

    def OnGraphGenerate(self, event):
        my_filename = self.m_graphic_manager.generate_graph_display()
        self.m_graphic_manager.reload_display(my_filename)

    def _create_controls(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.m_panel_node = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_node, wx.aui.AuiPaneInfo().Left().Caption(u"Nodes").CloseButton(
            False).Dock().Resizable().FloatingSize(wx.Size(200, 36)).Row(1).MinSize(wx.Size(200, 200)).Layer(0))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_search_node_ctrl = wx.SearchCtrl(self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_search_node_ctrl.ShowSearchButton(True)
        self.m_search_node_ctrl.ShowCancelButton(True)
        bSizer2.Add(self.m_search_node_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.m_list_node_ctrl = wx.ListView(
            self.m_panel_node, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(250, -1), wx.LC_REPORT)
        self.m_list_node_ctrl.InsertColumn(0, "No.", width=50)
        self.m_list_node_ctrl.InsertColumn(1, "Name", width=150)

        bSizer2.Add(self.m_list_node_ctrl, 1, wx.EXPAND, 5)

        self.m_panel_node.SetSizer(bSizer2)
        self.m_panel_node.Layout()
        bSizer2.Fit(self.m_panel_node)
        self.m_panel_main = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_main,
                           wx.aui.AuiPaneInfo().Center().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Movable(False).Dock().Resizable().FloatingSize(wx.DefaultSize).DockFixed(
                               True).BottomDockable(False).TopDockable(False).LeftDockable(False).RightDockable(
                               False).Floatable(False).CentrePane())

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_html_win = wx.html.HtmlWindow(self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.html.HW_SCROLLBAR_AUTO)
        bSizer3.Add(self.m_html_win, 1, wx.EXPAND, 5)
        # self.m_html_win = pdfViewer(
        #    self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #    wx.HSCROLL | wx.VSCROLL)
        # self.m_html_win.UsePrintDirect = False
        # self.m_SetSizerProps(expand=True, proportion=1)

        # wx.html.HtmlWindow(self.m_panel_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO)

        self.m_panel_main.SetSizer(bSizer3)
        self.m_panel_main.Layout()
        bSizer3.Fit(self.m_panel_main)
        self.m_panel_link = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_mgr.AddPane(self.m_panel_link, wx.aui.AuiPaneInfo().Right().Caption(u"Links").CloseButton(
            False).Dock().Resizable().FloatingSize(wx.Size(400, 250)).Row(1).Position(1).MinSize(wx.Size(200, 250)))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_search_link_ctrl = wx.SearchCtrl(self.m_panel_link, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_search_link_ctrl.ShowSearchButton(True)
        self.m_search_link_ctrl.ShowCancelButton(True)
        bSizer4.Add(self.m_search_link_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.m_list_link_ctrl = wx.ListCtrl(
            self.m_panel_link, wx.ID_ANY, wx.DefaultPosition,
            wx.DefaultSize, wx.LC_REPORT)
        self.m_list_link_ctrl.InsertColumn(0, "From", width=100)
        self.m_list_link_ctrl.InsertColumn(1, "To", width=100)

        bSizer4.Add(self.m_list_link_ctrl, 1, wx.EXPAND, 5)

        self.m_panel_link.SetSizer(bSizer4)
        self.m_panel_link.Layout()
        bSizer4.Fit(self.m_panel_link)

        # create the menubar / toolbar / statusbar
        self._create_menubar()
        self._create_toolbar()
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.m_mgr.Update()
        self.Centre(wx.BOTH)
