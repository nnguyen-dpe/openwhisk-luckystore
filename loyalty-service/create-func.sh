#!/bin/bash

docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

zip -r loyalty-service.zip virtualenv __main__.py

wsk -i action create loyalty-service --kind python:3 loyalty-service.zip
