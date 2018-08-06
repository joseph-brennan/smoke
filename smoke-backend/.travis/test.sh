#!/bin/bash

tox
coverage run --source smoke --omit smoke/manage.py,smoke/wsgi.py -m py.test
coverage report -m
coveralls --output=../coverage.json
(cd .. && coveralls --merge=coverage.json) || true # for local tests
