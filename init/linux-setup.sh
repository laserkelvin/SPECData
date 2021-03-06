#!/usr/bin/env bash
# linux-setup.cmd
# Jasmine N. Oliveira
# Installs the SPECdata environment in Anaconda
# and opens the setup Wizard for configuration

echo "Installing Conda Environment..."
conda env create -n specdata-env -f bin/conda_environment_linux.yml

echo "Open Environment.."
source activate specdata-env

echo "Running Setup Wizard..."
cd ..
python run_wizard.py

