from application import db
from sqlalchemy.sql import text
from application.models import Base


class Player(Base):

    __tablename__ = "player"
    
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
        stmt = text("SELECT Team.Name, Player.Name, Player.Number, Player.Position FROM Player, Team"
                    " WHERE Player.team_id = Team.id ORDER BY Player.Name, Player.Number, Player.Position, Team.id")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"name": row[0], "number": row[1], "position": row[2], "team_name": row[3]})

        return response


    @staticmethod
    def num_of_forwards():
        stmt = text("SELECT team.name, COUNT(player.position) AS Forward FROM player, team"
                    " WHERE player.team_id = team.id AND player.position IN ('VL','OL','KH') GROUP BY team.name")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"team_name": row[0], "forward": row[1]})

        return response

