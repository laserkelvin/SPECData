# windows-setup.ps1
# Jasmine N. Oliveira
#  Installs the SPECdata enviornment
#  and opens the Setup Wizard for configuration

echo "Installing Conda Environment..."
conda env create -n specdata-env -f bin/conda_environment_windows.yml

echo "Open Environment.."
activate specdata-env

echo "Running Setup Wizard..."
cd ..


python run_wizard.py
