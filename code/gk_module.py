#!/usr/bin/python

GK_SHAPE_TYPES = [
    "box",
    "ellipse",
    "diamond",
    "folder"
]


class GKModule(object):
    def __init__(self, name=None):
        """contain module definition"""
        self.m_name = name
        self.m_description = None
        self.m_shapetype = GK_SHAPE_TYPES[0]
        self.m_external_link = None

    def create_node(self, dot_obj):
        dot_obj.node(self.m_name, shape=self.m_shapetype)


