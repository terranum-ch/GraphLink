#!/urs/bin/python
import os
import wx

from .gkui_link_dlg import GKUILinkDialog


class GKUIGraphicManager(object):
    def __init__(self, parentframe, linklist, graphicview, nodemanager):
        self.m_link_list = linklist
        self.m_graphic_view = graphicview
        self.m_node_manager = nodemanager
        self.m_parent_frame = parentframe

    def add_link_dialog(self):
        my_dlg = GKUILinkDialog(self.m_graphic_view)
        my_dlg.ShowModal()
