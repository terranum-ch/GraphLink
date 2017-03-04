#!/usr/bin/python


class GKLink(object):
    def __init__(self, node1, node2, label=None, color=None):
        self.m_node1 = node1
        self.m_node2 = node2
        self.m_label = label
        self.m_color = color

    def create_link(self, dot_obj):
        """create a link between two nodes"""
        if dot_obj is None:
            return False
        dot_obj.edge(
            self.m_node1.m_name,
            self.m_node2.m_name,
            label=self.m_label,
            color=self.m_color)
        return True
