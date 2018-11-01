#!/bin/bash
HOST="$1"
echo "Invoking function with an order"
curl --insecure -X POST \
  "https://$HOST/api/v1/web/guest/default/order-api/api/v1/orders" \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "test",
    "customer_name": "Lucky Sushi"
}'