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

    penalty_receiver = db.relationship('Penalty', backref = 'penalty_receiver', lazy = 'dynamic', foreign_keys = 'Penalty.receiver_id')

    def __init__(self, name, number, position, team_id):
        self.name = name
        self.number = number
        self.position = position
        self.team_id = team_id

    @staticmethod
    def all_players():
        stmt = text("SELECT Team.Name, Player.id, Player.Name, Player.Number, Player.Position FROM Player, Team"
                    " WHERE Player.team_id = Team.id ORDER BY Team.id, Player.Name, Player.Number, Player.Position")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"team_name": row[0], "id": row[1], "name": row[2], "number": row[3], "position": row[4]})

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
    def team_players(p_team_id):

        stmt = text("SELECT number, name FROM Player"
                    " WHERE team_id = :p_team_id").params(p_team_id=p_team_id)
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
    
    @staticmethod
    def player_total_points():

        stmt = text("SELECT player.name, team.name, COUNT(*) AS points "
                    " FROM player, team, goal "
                    " WHERE player.team_id = team.id "
                    " AND (player.id = goal.scorer_id OR player.id = goal.assistant_1_id OR player.id = goal.assistant_2_id) "
                    " GROUP BY player.name, team.name ORDER BY points DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"player_name": row[0], "team_name": row[1], "points": row[2]})

        return response

    @staticmethod
    def player_goals():

        stmt = text("SELECT player.name, team.name, COUNT(*) AS goals "
                    " FROM player, team, goal "
                    " WHERE player.team_id = team.id "
                    " AND player.id = goal.scorer_id "
                    " GROUP BY player.name, team.name ORDER BY goals DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"player_name": row[0], "team_name": row[1], "num_of_goals": row[2]})

        return response

    @staticmethod
    def player_assists():

        stmt = text("SELECT player.name, team.name, COUNT(*) AS assists "
                    " FROM player, team, goal "
                    " WHERE player.team_id = team.id "
                    " AND (player.id = goal.assistant_1_id OR player.id = goal.assistant_2_id) "
                    " GROUP BY player.name, team.name ORDER BY assists DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"player_name": row[0], "team_name": row[1], "assists": row[2]})

        return response

    @staticmethod
    def player_penalties():

        stmt = text("SELECT player.name, team.name, SUM(CAST(penalty.length AS INT)) AS minutes "
                    " FROM player, team, penalty "
                    " WHERE player.team_id = team.id "
                    " AND player.id = penalty.receiver_id "
                    " GROUP BY player.name, team.name ORDER BY minutes DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"player_name": row[0], "team_name": row[1], "minutes": row[2]})

        return response

    @staticmethod
    def delete_player(id):

        stmt = text("DELETE FROM goal WHERE scorer_id = :id OR assistant_1_id = :id OR assistant_2_id = :id").params(id=id)
        db.engine.execute(stmt)

        # stmt = text("DELETE FROM penalty WHERE receiver_id = :id").params(id=id)
        # db.engine.execute(stmt)

        # stmt = text("DELETE FROM player WHERE id = :id").params(id=id)
        # db.engine.execute(stmt)        
