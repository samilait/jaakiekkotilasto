from application import db
from sqlalchemy.sql import text
from application.models import Base


class Team(Base):

    __tablename__ = "team"

    name = db.Column(db.String(250), nullable=False)

    player = db.relationship("Player", backref='team', lazy=True)
    
    home_team = db.relationship('Match', backref = 'home_team', lazy = 'dynamic', foreign_keys = 'Match.home_team_id')
    away_team = db.relationship('Match', backref = 'away_team', lazy = 'dynamic', foreign_keys = 'Match.away_team_id')

    goal_team = db.relationship('Goal', backref = 'goal_team', lazy = 'dynamic', foreign_keys = 'Goal.team_id')
    penalty_team = db.relationship('Penalty', backref = 'penalty_team', lazy = 'dynamic', foreign_keys = 'Penalty.team_id')

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
    
    
    @staticmethod
    def all_team_data():

        # stmt = text("SELECT Team.id, Team.Name FROM Team")
        stmt = text("SELECT id, name FROM Team")
                    
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append((row[0], row[1]))

        return response
    
    @staticmethod
    def team_goals():

        stmt = text("SELECT team.name, COUNT(*) AS home "
                    " FROM team, goal "
                    " WHERE goal.team_id = team.id "
                    " GROUP BY team.name ORDER BY home DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"team_name": row[0], "goals_scored": row[1]})

        return response

    @staticmethod
    def team_penalties():

        stmt = text("SELECT team.name, SUM(CAST(penalty.length AS INT)) AS minutes "
                    " FROM team, penalty "
                    " WHERE penalty.team_id = team.id "
                    " GROUP BY team.name ORDER BY minutes DESC")

        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            response.append({"team_name": row[0], "minutes": row[1]})

        return response

