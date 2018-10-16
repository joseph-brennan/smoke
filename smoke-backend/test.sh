#!/bin/bash
echo -n Collection packages...
pip install -q -r requirements-dev.txt
echo ' Done'
tox -e py37
