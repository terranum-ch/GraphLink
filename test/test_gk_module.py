#!/urs/bin/python

import os
import sys
import pytest
import graphviz

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "code"))
from gk_module import *


def test_graphviz():
    dot = graphviz.Digraph(comment='test_graph')
    dot.node("A")
    dot.node("B")
    dot.node("C")
    dot.edges(['AB', 'BC'])
    dot.render()


def test_gkmodule():
    mym1 = GKModule("test1")
    mym2 = GKModule("test2")

    dot = graphviz.Digraph(comment='test_graph2')
    mym1.create_node(dot)
    mym2.create_node(dot)
    dot.edge('test1', 'test2')
    dot.render()


