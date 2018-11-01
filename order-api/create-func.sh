#!/bin/bash

# build dependencies with openwhisk python runtime
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

# pack for deployment
zip -r order-api.zip __main__.py app.py apis flaskwsk virtualenv requirements.txt README.md

# create action with execution time of 500 millis & memory of 128MB
wsk -i action create order-api --kind python:3 order-api.zip --web raw -t 500 -m 128

# get callable action url
wsk -i action get order-api --url
