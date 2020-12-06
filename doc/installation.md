# GraphLink installation

Requirements : 
 - Python3
 - wxWidgets
 - graphviz
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

## Graphviz

Install the graphviz binary:
    - Linux : `sudo apt-get install graphviz`
    - OSX : `brew install graphviz`
    - Windows : `choco install graphviz`

It's also possible to put all the binaries into the /lib/bin folder. If this folder exists, GraphLink will use it.

## Test

Run the test with `pytest` in the root directory

## Binary

Run the following command :

    pyinstaller --onefile --windowed --name=GraphLink --icon=resources/art/graphlink.icns main.py

edit the `GraphLink.spec` file and add the following in the data line : 

    datas=[('../trunk/graphlink/art/*.png', 'art')],

run :

     pyinstaller GraphLink.spec



