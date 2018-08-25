#!/bin/bash
pip install -r requirements.txt
pip install -e .
smoke_backend init
flask run -h 0.0.0.0 -p 8000
