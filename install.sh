# Installs dependencies from requirements.txt
echo """
================================================================================
Installing Dependencies...
================================================================================
"""
# reads packages from txt file and installs them with pip
pip install -r requirements.txt

echo """
================================================================================
Packages successfully installed!
================================================================================
"""
