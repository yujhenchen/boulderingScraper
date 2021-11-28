#!/bin/bash

# Update conda to the latest
conda update conda
conda --version

# Remove the envronment
# conda remove - name myenv - all
# Create new python environment with specific python version
conda create --name myenv -y python=3.10.0

# Activate environment (Set as working environment)
# conda activate myenv
# conda init
activate myenv # For windows

# Install packages using conda on working conda environment
conda install --name myenv -y -c conda-forge selenium
conda install --name myenv -y -c conda-forge webdriver-manager
conda install --name myenv -y -c conda-forge pytest-html

# Check installed packages
# conda list

# List all current installed Python versions
# conda search -f python

# Check current working environment
conda info --envs

# Check installed packages of specific working environment
conda list --name myenv
