
#--- SETUP -----------------------------------------------#

eigen_ver := 3.3.5
pybind11_ver := 2.2.4

SHELL := /bin/bash


.PHONY: clean
clean:
	find . \( -name __pycache__ \
		-o -name "*.pyc" \
		-o -name .pytest_cache \
		-o -path "./build" \
		-o -path "./dist" \
		-o -path "./nb_cpp.egg-info" \
		! -path ".venv/*" \
	\) -exec rm -rf {} +


#--- DEV -------------------------------------------------#

.PHONY: install-dev
install-dev:
	pip install -e .[dev]

.PHONY: fetch
fetch: fetch-eigen fetch-pybind11

.PHONY: fetch-eigen
fetch-eigen:
	curl -L https://github.com/eigenteam/eigen-git-mirror/archive/$(eigen_ver).tar.gz | tar zx && mv eigen-git-mirror-$(eigen_ver) eigen

.PHONY: fetch-pybind11
fetch-pybind11:
	curl -L https://github.com/pybind/pybind11/archive/v$(pybind11_ver).tar.gz | tar zx && mv pybind11-$(pybind11_ver) pybind11

.PHONY: build
build:
	mkdir -p build && \
	cd build && \
	cmake -DPYTHON_EXECUTABLE:FILEPATH=`which python` .. && \
	make && \
	cp *.so ../

.PHONY: build-dist
build-dist: clean
	python setup.py sdist

.PHONY: publish-dev
publish-dev:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: test
test:
	pytest test


#--- PROD-------------------------------------------------#

.PHONY: install
install:
	pip install .

.PHONY: publish-prod
publish-prod:
	twine upload dist/*
