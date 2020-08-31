from sqlalchemy.exc import IntegrityError

from app.main import db
from app.main.model.positions import Positions


def save_positions(data, user):
    if not user or data == {}:
        response_object = {
                'status': 'fail',
                'message': 'Positions is empty'
            }
        return response_object, 400

    positions_entries = []
    for position in data['positions']:
        new_entry = Positions(user_id=user.id, **position)
        positions_entries.append(new_entry)

    # register data to bdd
    db.session.add_all(positions_entries)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        response_object = {
                    'status': 'fail',
                    'message': 'Conflict timestamps is registred'

                }
        return response_object, 409

    response_object = {
                'status': 'success',
            }
    return response_object, 201


def get_all_positions(user):
    positions = Positions.query.filter_by(user_id=user.id).all()
    return positions, 200
