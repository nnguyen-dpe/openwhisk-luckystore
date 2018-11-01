### Create python action as handler

```sh
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash \
  -c "cd tmp && virtualenv virtualenv --python=python3 && source virtualenv/bin/activate && pip install -r requirements.txt"

zip -r inventory-service.zip virtualenv __main__.py

wsk -i action create inventory-service --kind python:3 inventory-service.zip
```

### Connect action and the order trigger
```sh
wsk -i rule create OrderEventRule_Inventory OrderKafkaTrigger inventory-service
```

### Verify that the action was invoked by checking the most recent activation.
```sh
wsk -i activation list --limit 1 inventory-service
wsk -i activation result {activation_id}
```

