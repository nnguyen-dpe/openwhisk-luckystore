### Create python action as handler

```sh
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

zip -r loyalty-service.zip virtualenv __main__.py

wsk -i action create loyalty-service --kind python:3 loyalty-service.zip
```

### Connect action and the order trigger
```sh
wsk -i rule create OrderEventRule_Loyalty OrderKafkaTrigger loyalty-service
```

### Verify that the action was invoked by checking the most recent activation.
```sh
wsk -i activation list --limit 1 loyalty-service
wsk -i activation result {activation_id}
```

