#!/urs/bin/python
import os
import wx

from ..core.gk_node import GKNode
from .gkui_node_dlg import GKUINodeEditDialog


class GKUINodeManager(object):
    def __init__(self, parentframe, listctrl):
        self.m_listctrl = listctrl
        assert (self.m_listctrl is not None), "listctrl is None!"
        self.m_parent_frame = parentframe
        self.m_nodes = []
        self.m_node_paths = []

    def add_node_path(self, nodepath):
        """specify search path for nodes"""
        if nodepath not in self.m_node_paths:
            self.m_node_paths.append(nodepath)

    def has_node_paths(self):
        """return True if some nodes path are defined"""
        if len(self.m_node_paths) == 0:
            return False
        return True

    def add_node_to_list(self, node):
        """add node to the internal list if it isn't already present"""
        if node not in self.m_nodes:
            self.m_nodes.append(node)

    def get_node_count(self):
        """get the number of nodes"""
        return len(self.m_nodes)

    def reload_path(self):
        """clear the list ctrl and parse the node paths"""
        for path in self.m_node_paths:
            if os.path.exists(path) is False:
                wx.LogError("{} didn't exist!".format(path))
            else:
                for myfile in os.listdir(path):
                    if myfile.endswith(".gkn"):  # node files
                        node = GKNode()
                        if node.load_from_file(myfile) is False:
                            wx.LogWarning("Error loading: {}".format(myfile))
                        else:
                            self.add_node_to_list(node)

                # reload the node list
                self.reload_list()

    def reload_list(self):
        """reload the node list"""
        self.m_listctrl.DeleteAllItems()
        for index, node in enumerate(self.m_nodes):
            self.m_listctrl.Append([index + 1, node.m_name])

    def add_node_dialog(self):
        """display the add node dialog"""
        mynode = GKNode()
        myDlg = GKUINodeEditDialog(self.m_parent_frame, mynode)
        if myDlg.ShowModal() == wx.ID_SAVE:
            self.add_node_to_list(mynode)
            self.reload_list()

    def edit_node_dialog(self):
        """display the edit node dialog"""
        my_node_index = self.m_listctrl.GetFirstSelected()
        if my_node_index == -1:
            wx.LogWarning("Nothing selected, select à node first!")
            return False

        my_node = self.m_nodes[my_node_index]
        assert(my_node)

        myDlg = GKUINodeEditDialog(self.m_parent_frame, my_node)
        if myDlg.ShowModal() == wx.ID_SAVE:
            self.reload_list()



