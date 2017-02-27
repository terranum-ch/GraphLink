#!/usr/bin/python

import os

GK_SHAPE_TYPES = [
    "box",
    "ellipse",
    "diamond",
    "folder",
    "image"
]


class GKModule(object):
    def __init__(self, name=None, image=None):
        """contain module definition"""
        self.m_name = name
        self.m_description = None
        self.m_shapetype = GK_SHAPE_TYPES[0]
        self.m_external_link = None
        if image is not None:
            self.set_image(image)

    def create_node(self, dot_obj):
        """create a node using the specified parameters"""
        if self.m_shapetype is GK_SHAPE_TYPES[4]:  #image
            dot_obj.node(
                name=self.m_name,
                image=self.m_external_link,
                labelloc="b",
                shape="box")
        else:
            dot_obj.node(self.m_name, shape=self.m_shapetype)

    def set_image(self, imagepath):
        """Select an image for the node"""
        abs_img_path = os.path.abspath(imagepath)
        if os.path.exists(abs_img_path) is True:
            self.m_shapetype = GK_SHAPE_TYPES[4]  # image
            self.m_external_link = os.path.abspath(imagepath)
            return True
        else:
            self.m_shapetype = GK_SHAPE_TYPES[0]
            self.m_external_link = None
        return False


