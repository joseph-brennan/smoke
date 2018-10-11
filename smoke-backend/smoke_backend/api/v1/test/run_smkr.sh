#!/bin/sh

docker build -t test . 
docker run --rm test 