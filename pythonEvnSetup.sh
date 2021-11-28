#!/bin/bash

pip install --upgrade pip

# Setup and init virtual environment as working environment
pip install virtualenv
python -m venv .
. Scripts/activate

# Install packages using pip
pip install selenium --upgrade
pip install webdriver-manager
pip install pytest-html

pip list