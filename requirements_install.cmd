@echo off
rem ------------------------------------------------------------------------------------------------
rem
rem Install the python libraries needed for this projects from requirements.txt
rem
rem Autor: Heribert Füchtenhans
rem
rem ------------------------------------------------------------------------------------------------

set AllwaysArgs=--trusted-host files.pythonhosted.org --trusted-host pypi.org --retries 1 --upgrade

rem set up virtual environment
call .\.venv\Scripts\Activate.bat

python.exe -m pip install %AllwaysArgs% --upgrade pip
pip3 install %AllwaysArgs% -r requirements.txt

echo.
pause
