# Define api routes for namespace
import logging
import time

from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime
from apis.api import api
from apis.views import _order, _err, ApiError
from apis.service import _srv
from apis.exceptions import NotFoundException, InvalidRequestException

ns = Namespace(
    name='orders', 
    description="Order related operations"
)

log = logging.getLogger(__name__)

@ns.route('/orders')
@api.response(400, 'Invalid request', _err)
@api.response(500, 'Internal server error', _err)
class DeveloperCollection(Resource):
    @api.expect(_order)
    @api.doc(description='Create a new order', id='createOrder')
    def post(self, **kwargs):        
        try:
            data = request.json
            return _srv.create(data), 201
        except:
            return {
                'errorCode': 'InvalidRequest',
                'errorDescription': 'Bad'
            }, 400


@ns.route('/health')
class HealthCheck(Resource):
    @api.response(200, 'Health check ok')
    def get(self):
        return {
            'message': 'Health checked at: ' + str(datetime.now())
        }, 200
