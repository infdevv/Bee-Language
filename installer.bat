@echo off

rem Set up an alias for the desired Python command

rem Get the full path to the directory of this batch script
set "scriptDir=%~dp0"

rem Set up an alias for the desired Python command with the full path
doskey bs=python "%scriptDir%index.py" $*

rem Now you can use "bs code.bee" to execute "python index.py code.bee" from any location
