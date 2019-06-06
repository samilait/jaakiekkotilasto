from application import db
from sqlalchemy.sql import text


class Player(db.Model):

    __tablename__ = "player"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    number = db.Column(db.Integer)
    position = db.Column(db.String(4), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, name, number, position, team_id):
        self.name = name
        self.number = number
        self.position = position
        self.team_id = team_id

    @staticmethod
    def all_players():
        stmt = text("SELECT Player.Name, Player.Number, Player.Position, Team.Name FROM Player, Team"
                    " WHERE Player.team_id = Team.id GROUP BY Team.id")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"name": row[0], "number": row[1], "position": row[2], "team_name": row[3]})

        return response
