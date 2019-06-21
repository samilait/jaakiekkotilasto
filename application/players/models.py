from application import db
from sqlalchemy.sql import text
from application.models import Base


class Player(Base):

    __tablename__ = "player"
    
    name = db.Column(db.String(250), nullable=False)
    number = db.Column(db.Integer)
    position = db.Column(db.String(4), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    goal_scorer = db.relationship('Goal', backref = 'goal_scorer', lazy = 'dynamic', foreign_keys = 'Goal.scorer_id')
    goal_assistant_1 = db.relationship('Goal', backref = 'goal_assistant_1', lazy = 'dynamic', foreign_keys = 'Goal.assistant_1_id')
    goal_assistant_2 = db.relationship('Goal', backref = 'goal_assistant_2', lazy = 'dynamic', foreign_keys = 'Goal.assistant_2_id')

    def __init__(self, name, number, position, team_id):
        self.name = name
        self.number = number
        self.position = position
        self.team_id = team_id

    @staticmethod
    def all_players():
        stmt = text("SELECT Team.Name, Player.Name, Player.Number, Player.Position FROM Player, Team"
                    " WHERE Player.team_id = Team.id ORDER BY Team.id, Player.Name, Player.Number, Player.Position")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"team_name": row[0], "name": row[1], "number": row[2], "position": row[3]})

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


    @staticmethod
    def team_players(team_id):

        stmt = text("SELECT Player.number, Player.name FROM Player"
                    " WHERE Player.team_id = :team_id").params(team_id=team_id)
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append((row[0], row[1]))

        return response
    
    @staticmethod
    def find_player_id(player_name=""):

        stmt = text("SELECT Player.id FROM Player"
                    " WHERE Player.name = :player_name").params(player_name=player_name)
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append(row[0])

        return response



