@echo off 

cd .. 

rem xcopy installer\index.py to compiler\index.py after deleting compiler\index.py

del compiler\index.py

xcopy installer\index.py compiler\index.py
