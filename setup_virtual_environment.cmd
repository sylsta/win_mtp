@echo off
rem ------------------------------------------------------------------------------------------------
rem
rem Create a virtual environment if it doesn't exist and start powershell with the virtual
rem environemnt
rem
rem Autor: Heribert Füchtenhans
rem
rem ------------------------------------------------------------------------------------------------

if not exist venv (
	echo venv doesn't exist so I create the virtual environment
	@REM python -m venv --system-site-packages .venv
	python -m venv venv --system-site-packages
)
call .\venv\Scripts\activate.bat
cmd /K
