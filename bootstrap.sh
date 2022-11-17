#!/bin/sh
export FLASK_APP=./camerapipeline/index.py
pipenv run flask --debug run -h 0.0.0.0