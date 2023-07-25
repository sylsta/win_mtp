@echo off
rem ------------------------------------------------------------------------------------------------
rem
rem Create the documentation with mkdocs
rem
rem Autor: Heribert Füchtenhans
rem
rem ------------------------------------------------------------------------------------------------

rem set up virtual environment
call .\.venv\Scripts\Activate.bat

@REM mkdocs build

echo.
echo Upload documentation to github?
pause

mkdocs gh-deploy

echo.
echo Create local documentation that can be opend in local browser
pause

mkdocs build --no-directory-urls

echo.
pause
