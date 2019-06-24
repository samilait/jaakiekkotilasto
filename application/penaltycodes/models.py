from application import db
from sqlalchemy.sql import text
from application.models import Base


class PenaltyCode(Base):

    __tablename__ = "penaltycode"

    code = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    penalty = db.relationship("Penalty", backref='penaltycode', lazy=True)
    
    def __init__(self, code, description):
        self.code = code
        self.description = description

    @staticmethod
    def all_penaltycode_data():

        stmt = text("SELECT id, code, description FROM Penaltycode ORDER BY description, code, id")
                    
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            desc_code = row[2] + " (" + row[1] + ")"
            response.append((row[0], desc_code))

        return response

    @staticmethod
    def find_penaltycode_id(penalty_code):

        stmt = text("SELECT id FROM Penaltycode"
                    " WHERE code = :penalty_code").params(penalty_code=penalty_code)
                    
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append(row[0])

        return response
