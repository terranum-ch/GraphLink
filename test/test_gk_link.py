#!/urs/bin/python

import os
import sys
import pytest
import graphviz

curdir = os.path.dirname(__file__)
sys.path.append(os.path.join(curdir, ".."))

from graphlink.core.gk_link import GKLink
from graphlink.core.gk_node import GKNode


def test_gk_link_init():
    myn1 = GKNode("node1")
    myn2 = GKNode("node2")
    myl1 = GKLink(myn1, myn2)
    assert myl1.m_node1 == myn1
    assert myl1.m_node2 == myn2


def test_gk_link_simple():
    myn1 = GKNode("node1")
    myn2 = GKNode("node2")
    myn3 = GKNode("node3")
    myl1 = GKLink(myn1, myn2)
    myl2 = GKLink(myn1, myn3, "important", "red")
    myl3 = GKLink(myn2, myn3)

    # graphic part
    dot = graphviz.Digraph(comment='test_graph')
    myn1.create_node(dot)
    myn2.create_node(dot)
    myn3.create_node(dot)

    myl1.create_link(dot)
    myl2.create_link(dot)
    myl3.create_link(dot)
    dot.render(filename="test_link1.gv")



