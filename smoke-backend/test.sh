#!/bin/bash
echo -n Collecting packages...
pip install -q -r requirements-dev.txt
echo ' Done'
tox
