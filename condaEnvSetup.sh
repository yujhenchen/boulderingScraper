#!/bin/bash

# Update conda to the latest
conda update -y conda
conda --version

# Remove the envronment
# conda remove - name myenv - all
# Create new python environment with specific python version
conda create --name myenv -y python=3.8

# Install packages using conda on working conda environment
conda install --name myenv -y -c conda-forge selenium
conda install --name myenv -y -c conda-forge webdriver-manager
conda install --name myenv -y -c conda-forge pytest-html
conda install --name myenv -y -c conda-forge django
conda install --name myenv -y -c conda-forge backports.zoneinfo

# Activate environment (Set as working environment)
# conda activate myenv
# conda init
conda activate myenv # For windows

# Check installed packages
# conda list

# List all current installed Python versions
# conda search -f python

# Check current working environment
conda info --envs

# Check installed packages of specific working environment
conda list --name myenv
