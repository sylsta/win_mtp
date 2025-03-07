#!/bin/bash

# ------------------------------------------------------------------------------------------------
#
# Create a virtual environment if it doesn't exist and start bash with the virtual
# environment
#
# Author: Heribert Füchtenhans
#
# ------------------------------------------------------------------------------------------------

# which python exec full path ?
# since some distros eg. Debian do not have python alias
python_exec=$(command -v python3 || command -v python)

# Check python version
python_version=$($python_exec --version 2>/dev/null | awk '{print $2}')

if [[ -z "$python_version" ]]; then
    echo "Python is not installed."
else
	if [ "$(printf '%s\n%s\n' "3.12" "$python_version" | sort -V | tail -n1)" == "$python_version" ]; then
		if [ ! -d ./venv_linux ]; then
			echo "venv_linux doesn't exist so I create the virtual environment"
			$python_exec -m venv ./venv_linux

			echo "Install requirements"
			source ./venv_linux/bin/activate
			AllwaysArgs='--trusted-host files.pythonhosted.org --trusted-host pypi.org --retries 1 --upgrade'
			$python_exec -m pip install $AllwaysArgs --upgrade pip
			pip install $AllwaysArgs -r requirements.txt
		fi
		bash --rcfile "./venv_linux/bin/activate" -i
    else
        echo "Python version too old: $python_exec - $python_version"
    fi
fi
