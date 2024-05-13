@echo off
python3 -m PyInstaller --onefile main.py
del main.py
del main.spec