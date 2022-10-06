#!/bin/bash

pyinstaller --hidden-import 'pyautogui' --onefile 'legal_plotter.py'

read -p "Press enter to continue... "

