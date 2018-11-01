import uuid
import logging
import json
from kafka import KafkaProducer

log = logging.getLogger(__name__)

class OrderService(object):

    def __init__(self):
        self.__topic = "order-service-topic"
        self.__producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def create(self, data):
        data['id'] = str(uuid.uuid4())
        self.__producer.send(self.__topic, data)
        return data['id']

_srv = OrderService()