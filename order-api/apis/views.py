# Rest view model for api requests and responses
from flask_restplus import fields
from apis.api import api
from apis.exceptions import ApiError

_order = api.model('Order', {
    'id': fields.String(required=False, readOnly=True),
    'customer_name': fields.String(required=True, min_length=3, max_length=200),
    'created_at': fields.String(required=False, readOnly=True)
})

_err = api.model('Error', {
    'errorCode': fields.String(required=True, description='Error types',
                               enum=ApiError._member_names_),
    'errorDescription': fields.String(required=True)
})
