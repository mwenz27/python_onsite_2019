#
# In your CodingNomads folder create a new folder. Inside of that folder:
#
# 1. Create a new virtual environment

python3 -m venv .venv
# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install at least 3 packages in the virtual environment.
pip install brew
pip install InstagramAPI
pip install md5hash
# 4. Freeze the installed packages to a requirements.txt file.

pip freeze > requirements.txt
# 5. Deactivate the virtual environment.

deactivate
# 6. Delete the virtual environment.
rm -rf <folder>

# 7. Create a new virtual environment and install the packages from the requirements.txt file.
#

