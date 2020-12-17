#!/urs/bin/python
import os
import wx
import tempfile

from .gkui_link_dlg import GKUILinkDialog
from ..core.gk_link import GKLink
from ..core.gk_graphic import GKGraphic


class GKUIGraphicManager(object):
    def __init__(self, parentframe, linklist, display, nodemanager):
        self.m_link_list = linklist
        self.m_display = display
        self.m_node_manager = nodemanager
        self.m_parent_frame = parentframe
        self.m_links = []

    def add_link_dialog(self):
        """display the link dialog"""
        myLink = GKLink(None, None)
        my_dlg = GKUILinkDialog(self.m_display, self.m_node_manager, myLink)
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

    def generate_graph_display(self):
        """create the graphic for the display"""
        graph = GKGraphic()
        for link in self.m_links:
            graph.add_link(link)

        my_temp_name = tempfile.mkstemp('.png', 'graphiclink')[1]

        graph.render(
            os.path.splitext(my_temp_name)[0],
            extension="png",
            size=self.m_display.GetSize()[0])
        return my_temp_name
        # TODO: Store the generated file and try to destroy it
        # when a new graph is created

    def reload_display(self, imgpath):
        self.m_display.SetPage("""
        <html>
        <body>
        <img src="{}"/>
        </body>
        </html>
        """.format(imgpath))
