install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv  \Codes/*.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=\Codes/.*?py \Codes/*.py

all: install lint format test
