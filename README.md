# Legal Plotter
###### Macro Build 1.0

## Overview
In the legal, surveying, and civil engineering fields, real estate properties are described by specifying the length, bearing, and radius of lines and arcs of the outer property line. When you start working on a project, the first thing you often do is take these legal descriptions and plot them into a CAD software. It can be quite tedious to do this by hand, and I knew there had to be a better way to do this. 

Hence, Legal Plotter was created. This project takes a legal description as input and plots it into AutoCAD for you!

## Development Environment
* __Visual Studio Code (IDE):__ An IDE with great support for Python.
* __Python 3.9.7:__ Python is a programming language, which this whole program was developed in.
* __RE:__ Regular Expression is a library built into Python which provides many options for searching through text. This was used to collect the necessary information from the legal description.
* __PyAutoGUI:__ This is a library which allows Python to simulate mouse and keyboard input, which is how this software communicates with AutoCAD
* __Py2exe:__ This is a library that enables saving a python file as an executable file, so this program can be run on any computer without needing to have Python installed.

## Future Work
* Translate this program into C# so that it can be built as a plugin to AutoCAD
* Make it able to handle more errors in the legal description typing (replacing a "0" with an "O", etc.)