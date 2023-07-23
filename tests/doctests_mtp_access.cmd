@echo off
cls
pushd ..\src\win_mtp
python -m doctest mtp_access.py
popd
pause
