install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=Code test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=.*?py Code/*.py

all: install lint format test
