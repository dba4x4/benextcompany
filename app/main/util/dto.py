from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True,
                               description='user email address'),

        'username': fields.String(required=True,
                                  description='user username'),

        'password': fields.String(required=True,
                                  description='user password'),

        'public_id': fields.String(required=False,
                                   description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True,
                               description='The email address'),

        'password': fields.String(required=True,
                                  description='The user password'),
    })


class PositionsDto:
    api = Namespace('positions', description='data related operations')
    positions_model = api.model('positions', {
        'latitudeE7': fields.Integer(required=True,
                                     description='Latitude coordinate'),

        'longitudeE7': fields.Integer(required=True,
                                      description='Longitude coordinate'),

        'altitude': fields.Integer(required=False,
                                   description='Altitude in meters'),

        'verticalAccuracy': fields.Integer(required=False,
                                           description='Vertical accuracy'),

        'accuracy': fields.Integer(required=True,
                                   description='Accuracy in meters'),

        'timestampMs': fields.Integer(required=True,
                                      description='Timestamp in ms'),
    })
    response_model = api.model("data", {
        'positions': fields.List(fields.Nested(positions_model)),
    })
