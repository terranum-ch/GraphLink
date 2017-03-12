#!/urs/bin/python
import os
import wx

from .gkui_link_dlg import GKUILinkDialog
from ..core.gk_link import GKLink


class GKUIGraphicManager(object):
    def __init__(self, parentframe, linklist, graphicview, nodemanager):
        self.m_link_list = linklist
        self.m_graphic_view = graphicview
        self.m_node_manager = nodemanager
        self.m_parent_frame = parentframe
        self.m_links = []

    def add_link_dialog(self):
        """display the link dialog"""
        myLink = GKLink(None, None)
        my_dlg = GKUILinkDialog(self.m_graphic_view, self.m_node_manager, myLink)
        if my_dlg.ShowModal() == wx.ID_OK:
            self.add_link_to_list(myLink)
            self.reload_list()

    def add_link_to_list(self, link):
        """add the link to the internal link list"""
        if link not in self.m_links:
            self.m_links.append(link)

    def reload_list(self):
        """reload the link list"""
        self.m_link_list.DeleteAllItems()
        for index, link in enumerate(self.m_links):
            self.m_link_list.Append([link.m_node1.m_name, link.m_node2.m_name])
