#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# copy Graphviz exe in lib/bin directory for a no-install build.
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib", "bin"))
if os.path.exists(lib_path):
    os.environ["PATH"] += os.pathsep + lib_path
    print (os.environ["PATH"])


OUTPUT_TEST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "output"))

import graphlink

