#!/bin/bash

docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

zip -r notification-service.zip virtualenv __main__.py

wsk -i action create notification-service --kind python:3 notification-service.zip