# Make file for yuan

PROJECT ?= yuan
PYENV_NAME = .venv
SHELL := /bin/bash

##############################
# yuan targets
##############################
.PHONY: run run-main yuan
run run-main yuan:
	@echo
	source ../$(PYENV_NAME)/bin/activate
	@echo "Entered Python3.7 virtual environment..."
	python3.7 main.py
	@echo
	@echo "- DONE: $@"

