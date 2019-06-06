from application import db
from sqlalchemy.sql import text

class Team(db.Model):

    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    player = db.relationship("Player", backref='team', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_team_id(team_name=""):
        stmt = text("SELECT Team.id FROM Team"
                    " WHERE Team.name = :team_name").params(team_name=team_name)
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append(row[0])

        return response
