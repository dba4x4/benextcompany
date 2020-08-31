from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from app.main.service.auth_helper import Auth

from ..util.dto import PositionsDto
from ..service.positions_service import save_positions, get_all_positions

api = PositionsDto.api
_positions = PositionsDto.response_model
_positions_models = PositionsDto.positions_model


@api.route('/')
class PositionsList(Resource):
    @token_required
    @api.response(200, 'Retrieve all positions for logged user.')
    @api.marshal_list_with(_positions_models)
    @api.doc('List all positions for user')
    def get(self):
        user = Auth.get_logged_user()
        return get_all_positions(user=user)

    @token_required
    @api.expect(_positions, validate=True)
    @api.response(201, 'Positions successfully created.')
    @api.response(409, 'Timestamp already exists.')
    @api.doc('create e new set of positions for logged user')
    def post(self):
        data = request.json
        user = Auth.get_logged_user()
        return save_positions(data=data, user=user)
