test:
	PYTHONPATH="$PYTHONPATH:." venv/bin/pytest -xs

install:
	virtualenv venv
	venv/bin/pip install -r requirements-dev.txt

clear:
	rm -rf venv

build:
	venv/bin/python setup.py sdist
	venv/bin/python python setup.py bdist_wheel

push: build
	venv/bin/twine upload dist/*

clean:
	rm -rf build dist q.egg-info
	find -name *.pyc -delete
	@- git status

deploy: push clean