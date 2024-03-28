# Python Environment Setup :

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# List of all installed packages and their versions

pip freeze > requirement.txt

# Show tree of all packages

poetry show --tree

# Run the application

python app.py

# Run the tests

pytest

# Run the linter

pylint app.py

# Run the formatter

black app.py

#
