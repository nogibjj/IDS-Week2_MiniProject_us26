install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv --cov=Code *.py

format:
	black Code/*.py

lint:
	pylint --disable=R,C --ignore-patterns=.*?py Code/*.py

all: install lint format test
