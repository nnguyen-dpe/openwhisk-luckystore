# Instruction

* Prerequisites:
> Install python3, pip3, virtualenv

* Setup:
```sh
git clone git@dpe.bitbucket.org:thebugspikers/order-api.git
cd order-api

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

* Test:
```sh

```

* Deploy to openwhisk:
```sh
# Run the following to install the dependencies and create a virtualenv using a compatible Docker image:
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

# Pack
zip -r order-api.zip __main__.py app.py apis flaskwsk virtualenv requirements.txt README.md

# Create action
wsk -i action create order-api --kind python:3 order-api.zip --web raw -t 15000
wsk -i action update order-api --kind python:3 order-api.zip --web raw

# Get action url
wsk -i action get order-api --url

curl https://{whisk.host}/api/v1/web/guest/default/order-api/api/v1/health
```