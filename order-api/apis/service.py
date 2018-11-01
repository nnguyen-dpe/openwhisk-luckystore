import uuid
import logging

log = logging.getLogger(__name__)

class OrderService(object):

    def __init__(self):
        pass

    def create(self, data):
        data['id'] = str(uuid.uuid4())
        return data['id']

_srv = OrderService()