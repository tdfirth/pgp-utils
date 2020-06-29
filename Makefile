.SILENT: build upload

build: src
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload --repository pypi dist/*

clean:
	rm -rf dist/ build/ __pycache__/ *.egg-info
