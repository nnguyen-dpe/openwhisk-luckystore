#!/bin/bash

docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

# pack
zip -r order-api.zip __main__.py app.py apis flaskwsk virtualenv requirements.txt README.md

# update action
wsk -i action update order-api --kind python:3 order-api.zip --web raw -t 500 -m 128

# get action url
wsk -i action get order-api --url