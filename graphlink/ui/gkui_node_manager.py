#!/urs/bin/python
import os
import wx

from ..core.gk_node import GKNode


class GKUINodeManager(object):
    def __init__(self, listctrl):
        self.m_listctrl = listctrl
        assert (self.m_listctrl is not None), "listctrl is None!"
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

    def reload(self):
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

        # reload the list here
        self.m_listctrl.DeleteAllItems()
        for index, node in enumerate(self.m_nodes):
            self.m_listctrl.InsertStringItem(index, node.m_name)


