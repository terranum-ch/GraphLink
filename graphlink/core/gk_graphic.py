#!/urs/bin/python

import os
import graphviz
# from gk_node import GKNode
# from gk_link import GKLink

class GKGraphic(object):
    """Manage graphic"""
    def __init__(self, label=None):
        self.m_label = label
        self.m_nodes_list = []
        self.m_link_list = []

    def add_link(self, link):
        """add link and related node to the diagram"""
        if link is None:
            return False

        self.m_link_list.append(link)
        if link.m_node1 not in self.m_nodes_list:
            self.m_nodes_list.append(link.m_node1)
        if link.m_node2 not in self.m_nodes_list:
            self.m_nodes_list.append(link.m_node2)
        return True

    def render(self, filename, extension="pdf", size=None):
        """generate the graphic and save result as an image"""
        if filename is None:
            return False

        if size:
            size_str = str(size / 100.0) + "!"
            dot = graphviz.Graph(comment=self.m_label, format=extension, graph_attr={"size": size_str})
        else:
            dot = graphviz.Graph(comment=self.m_label, format=extension)

        # create the nodes for the nodes_list items
        for node in self.m_nodes_list:
            node.create_node(dot)

        # create the link for the link list
        for link in self.m_link_list:
            link.create_link(dot)

        dot.render(filename, cleanup=True)
        return True






