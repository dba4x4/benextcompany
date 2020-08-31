from .. import db
import datetime


class Positions(db.Model):
    """
    Position model for storing data user related details
    """
    __tablename__ = "positions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer(),
                        db.ForeignKey('user.id', ondelete='CASCADE'))
    latitudeE7 = db.Column(db.Integer, nullable=False)
    longitudeE7 = db.Column(db.Integer, nullable=False)
    altitude = db.Column(db.Integer, nullable=True)
    verticalAccuracy = db.Column(db.Integer, nullable=True)
    accuracy = db.Column(db.Integer, nullable=True)
    timestampMs = db.Column(db.String(255), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Data for user id '{}' at '{}'>".format(self.user_id,
                                                        self.timestampMs)
