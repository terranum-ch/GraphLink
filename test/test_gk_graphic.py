#!/urs/bin/python

import os
import sys
import pytest

from .context import graphlink
from .context import OUTPUT_TEST_PATH

from graphlink.core.gk_link import GKLink
from graphlink.core.gk_node import GKNode
from graphlink.core.gk_node import GK_SHAPE_TYPE
from graphlink.core.gk_graphic import GKGraphic


def test_gk_graphic_simple():
    node1 = GKNode("Node1", shape=GK_SHAPE_TYPE[2])
    node2 = GKNode("Node2")
    myl1 = GKLink(node1, node2)

    graph = GKGraphic()
    assert graph.add_link(myl1) is True
    assert graph.render(os.path.join(OUTPUT_TEST_PATH, "test_graphic_result")) is True
    assert os.path.exists(os.path.join(OUTPUT_TEST_PATH, "test_graphic_result.pdf"))


def test_gk_graphic_image():
    node1 = GKNode("Node1", shape=GK_SHAPE_TYPE[2])
    node2 = GKNode("Node2")
    myl1 = GKLink(node1, node2)

    graph = GKGraphic()
    assert graph.add_link(myl1) is True
    assert graph.render(os.path.join(OUTPUT_TEST_PATH, "test_graphic_result"), extension="png", size=500) is True
    assert os.path.exists(os.path.join(OUTPUT_TEST_PATH, "test_graphic_result.png"))
