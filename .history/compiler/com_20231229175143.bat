@echo off
setlocal

rem Check if the user provided a filename as a command-line argument
if "%1"=="" (
    echo Please provide the filename as a command-line argument.
    echo Example: %~nx0 example.txt
    exit /b 1
)

rem Set the source file path in the site_packages directory
set "sourcePath=site_packages\%1"

rem Set the destination directory to the current working directory
set "destinationDir=%cd%"

rem Set the destination file path
set "destinationPath=%destinationDir%\%1"

rem Check if the source file exists
if not exist "%sourcePath%" (
    echo Source file not found: %sourcePath%
    exit /b 1
)

rem Copy the file
copy /Y "%sourcePath%" "%destinationPath%"

rem Check if the copy was successful
if errorlevel 1 (
    echo Failed to copy file.
    exit /b 1
)

echo File copied successfully from:
echo %sourcePath%
echo to:
echo %destinationPath%

endlocal
