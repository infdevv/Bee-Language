@echo off

rem Get the full path to the directory of this batch script
set "scriptDir=%~dp0"

rem Save the full path in config.ini (site_install_point)
set "site_install_point=%scriptDir%compiler"
echo site_install_point=%site_install_point% > compiler\config.ini

rem Change directory to site_packages and get the full path
pushd "%scriptDir%..\site-packages"
set "site_packages_point=%CD%"
popd

rem Append "/site_packages" to site_packages_point
set "site_packages_point=%site_packages_point%\compiler\site_packages"

rem Save the site_packages_point in config.ini
echo site_packages_point=%site_packages_point% >> compiler\config.ini

rem Set up an alias for the desired Python command with the full path
doskey bs=python.exe "%scriptDir%\compiler\index.py" $*

rem Now you can use "bs code.bee" to execute "python index.py code.bee" from any location

echo Finished installing!