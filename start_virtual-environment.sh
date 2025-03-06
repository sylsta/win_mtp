#!/bin/bash

# ------------------------------------------------------------------------------------------------
#
# Create a virtual environment if it doesn't exist and start powershell with the virtual
# environment
#
# Autor: Heribert Füchtenhans
#
# ------------------------------------------------------------------------------------------------

if [ ! -d ./venv_linux ]; then
	echo "venv_linux doesn't exist so I create the virtual environment"
	python3.12 -m venv ./venv_linux

	echo "Install requirements"
	source ./venv_linux/bin/activate
	AllwaysArgs='--trusted-host files.pythonhosted.org --trusted-host pypi.org --retries 1 --upgrade'
	python3.12 -m pip install $AllwaysArgs --upgrade pip
	pip3.12 install $AllwaysArgs -r requirements.txt
fi
bash --rcfile "./venv_linux/bin/activate" -i

