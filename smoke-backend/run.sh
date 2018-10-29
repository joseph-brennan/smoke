#!/bin/bash
pip install -q -r requirements.txt
pip install -q -e .
smoke_backend init
smoke_backend seed
flask run -h 0.0.0.0 -p 8000
