#!/bin/sh
echo $1

docker build -t test .
docker run --env STRING=$1 --rm test
