install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv --cov=main test_calc.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all: install lint format test
