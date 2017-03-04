#!/urs/bin/python

import os
import sys
import pytest

curdir = os.path.dirname(__file__)
sys.path.append(os.path.join(curdir, ".."))

from graphlink.core.gk_link import GKLink
from graphlink.core.gk_node import GKNode, GK_SHAPE_TYPE
from graphlink.core.gk_graphic import GKGraphic


def test_gk_graphic_simple():
    node1 = GKNode("Node1", shape=GK_SHAPE_TYPE[2])
    node2 = GKNode("Node2")
    myl1 = GKLink(node1, node2)

    graph = GKGraphic()
    assert graph.add_link(myl1) is True
    assert graph.render("test_graphic_result") is True

