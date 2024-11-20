include .env
export $(shell sed 's/=.*//' .env)
.PHONY: pull commit push install build publish genreqs downreqs installreqs clean

## Git

pull:
	git pull

commit: 
	git add .
	if [ -z "$(msg)" ]; then \
		git commit -m "update"; \
	else \
		git commit -m "$(msg)"; \
	fi

push: commit
	git push --set-upstream origin master

## Poetry Project

install:
	poetry install --no-root

build: clean
	poetry build

publish:
	if [ -z "$(PYPI_USERNAME)" ] || [ -z "$(PYPI_PASSWORD)" ]; then \
		echo "PYPI_USERNAME or PYPI_PASSWORD not found in ENVRIONMENT or .env file"; \
		exit 1; \
	fi
	poetry publish --username $(PYPI_USERNAME) --password $(PYPI_USERNAME)%  


## Requirements

genreqs:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

downreqs:
	if [ ! -d "vendor" ]; then \
		mkdir vendor; \
	fi
	if [ ! -f "requirements.txt" ]; then \
		echo "requirements.txt not found"; \
		exit 1; \
	fi
	poetry run pip download -r requirements.txt -d vendor

installreqs:
	if [ ! -d "vendor" ]; then \
		echo "vendor not found"; \
		exit 1; \
	fi
	poetry run pip install --no-index --find-links=vendor -r requirements.txt --no-deps


## Basic
clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	find . -name ".pytest_cache" -exec rm -rf {} \;
	find . -name ".DS_Store" -exec rm -rf {} \;


## Develop
run:
	poetry run python manage.py runserver 0.0.0.0:8000