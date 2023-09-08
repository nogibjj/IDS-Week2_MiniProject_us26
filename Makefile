install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	coverage run --source=plugin_module -m pytest -v test_*.py && coverage report -m

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all: install lint format test
