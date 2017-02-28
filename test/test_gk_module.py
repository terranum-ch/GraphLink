#!/urs/bin/python

import os
import sys
import pytest
import graphviz

curdir = os.path.dirname(__file__)
sys.path.append(os.path.join(curdir,".."))
print (os.path.join(curdir, "../graphlink"))

from graphlink.core.gk_node import GKNode
from graphlink.core.gk_node import GK_SHAPE_TYPES


@pytest.fixture()
def get_test_data_folder():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


def test_graphviz():
    dot = graphviz.Digraph(comment='test_graph')
    dot.node("A")
    dot.node("B")
    dot.node("C")
    dot.edges(['AB', 'BC'])
    dot.render(filename="test_graph1.gv")


def test_gknode():
    mym1 = GKNode("test1")
    mym2 = GKNode("test2")

    dot = graphviz.Graph(comment='test_graph2')
    mym1.create_node(dot)
    mym2.create_node(dot)
    dot.edge('test1', 'test2')
    dot.render(filename="test_graph2.gv")


def test_gknode_init():
    mym1 = GKNode()
    assert mym1.m_name is None
    assert mym1.m_description is None
    assert mym1.m_shapetype == GK_SHAPE_TYPES[0]
    assert mym1.m_external_link is None


def test_gknode_image(get_test_data_folder):
    mym1 = GKNode("Chief")
    assert mym1.set_image("not_existing_picture.png") is False

    img_path = os.path.join(get_test_data_folder, "person-icon.jpg")
    assert mym1.set_image(img_path) is True
    assert mym1.m_shapetype == GK_SHAPE_TYPES[4]  # image
    assert mym1.m_external_link == img_path

    mym3 = GKNode("John", img_path)
    assert mym3.m_external_link == img_path

    mym2 = GKNode("Bob", img_path)
    assert mym2.m_external_link == img_path
    mym4 = GKNode("+41791234567")

    # test printing with image
    dot = graphviz.Graph()

    mym1.create_node(dot)
    mym2.create_node(dot)
    mym3.create_node(dot)

    dot.edge(mym1.m_name, mym2.m_name)
    dot.edge(mym1.m_name, mym3.m_name)
    dot.edge(mym3.m_name, mym4.m_name)
    dot.edge(mym4.m_name, mym2.m_name)

    dot.render(filename="test_img1.gv")

