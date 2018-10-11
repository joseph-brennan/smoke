#!/bin/sh
echo $1
TST=$1

docker build -t test .
docker run --env TST_STRING=${TST} --rm test
