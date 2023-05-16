start: #start on linux mint
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python3 main.py


lint: #format
	pip freeze > requirements.txt
	black .
	isort .
	autopep8 ./ --recursive --in-place -a
# autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./




#	python -m venv .venv
#	source .venv/Scripts/activate
#	source .venv/bin/activate
#	python -m pip install --upgrade pip
#	pip install -r requirements.txt
