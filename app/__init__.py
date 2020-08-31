from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.positions_controller import api as positions_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TEST TECHNIQUE',
          version='0.1',
          authorizations={
            'apikey': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
                },
            },
          security='apikey'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(positions_ns)
