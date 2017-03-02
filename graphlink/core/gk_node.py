#!/usr/bin/python

import os
import pickle


GK_SHAPE_TYPE = [
    "box",
    "ellipse",
    "diamond",
    "folder",
    "image"
]


class GKNode(object):
    def __init__(self, name=None, image=None, shape=GK_SHAPE_TYPE[0]):
        """contain module definition"""
        self.m_name = name
        self.m_description = None
        self.m_shapetype = shape
        self.m_external_link = None
        if image is not None:
            self.set_image(image)

    def create_node(self, dot_obj):
        """create a node using the specified parameters"""
        if self.m_shapetype is GK_SHAPE_TYPE[4]:  # image
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
            self.m_shapetype = GK_SHAPE_TYPE[4]  # image
            self.m_external_link = os.path.abspath(imagepath)
            return True
        else:
            self.m_shapetype = GK_SHAPE_TYPE[0]
            self.m_external_link = None
        return False

    def save_to_file(self, filename=None):
        """Save the file to disk using filename
        return False if no filename is specified and
        m_name is None """
        if filename is None:
            filename = self.m_name
        # No filename, aborting
        if filename is None:
            return False

        with open(filename, 'wb') as f:
            pickle.dump([
                self.m_name,
                self.m_description,
                self.m_shapetype,
                self.m_external_link],
                f)
        return True

    def load_from_file(self, filename):
        """load node data from file"""
        if filename is None:
            return False

        if os.path.exists(filename) is False:
            return False

        with open(filename, 'rb') as f:
            [self.m_name,
                self.m_description,
                self.m_shapetype,
                self.m_external_link] = pickle.load(f)
        return True


