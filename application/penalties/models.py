from application import db
from sqlalchemy.sql import text
from application.models import Base


class Penalty(Base):

    __tablename__ = "penalty"

    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)    # Done
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)      # Done
    start_time = db.Column(db.String(5), nullable=False)
    length = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)           # Done
    penaltycode_id = db.Column(db.Integer, db.ForeignKey('penaltycode.id'), nullable=False)           # Done

    def __init__(self, match_id, team_id, start_time, length, end_time, receiver_id, penaltycode_id):
        self.match_id = match_id
        self.team_id = team_id
        self.start_time = start_time
        self.length = length
        self.end_time = end_time
        self.receiver_id = receiver_id
        self.penaltycode_id = penaltycode_id

    @staticmethod
    def get_penalty_id(penalty_code):

        stmt = text("SELECT Penalty.id FROM Penalty"
                    " WHERE Penalty.code = :penalty_code").params(penalty_code=penalty_code)
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append(row[0])

        return response

