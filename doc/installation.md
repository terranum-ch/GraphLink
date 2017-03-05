# GraphLink installation

Requirements : 
 - Python3
 - wxWidgets
 - graphwiz
 - pytest

## Virtualenv
Install using the following command :

    Python3 -m venv env
    source env/bin/activate (Unix)
    env\Scripts\activate (Windows)

## Dependencies

Install the required dependencies with pip

    pip install pytest, graphviz
    pip install -U --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython_Phoenix


## Test

Run the test with `pytest` in the root directory

## Binary

Run the following command :

    pyinstaller --onefile --windowed --name=GraphLink --icon=resources/art/graphlink.icns main.py

edit the `GraphLink.spec` file and add the following in the data line : 

    datas=[('../trunk/graphlink/art/*.png', 'art')],

run :

     pyinstaller GraphLink.spec



