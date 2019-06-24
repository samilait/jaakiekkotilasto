from application import db
from sqlalchemy.sql import text
from application.models import Base
import datetime


class Match(Base):

    __tablename__ = "match"

    match_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_team_score = db.Column(db.Integer)
    away_team_score = db.Column(db.Integer)

    match_goal = db.relationship('Goal', backref = 'match_goal', lazy = 'dynamic', foreign_keys = 'Goal.match_id')

    match_penalty = db.relationship('Penalty', backref = 'match_penalty', lazy = 'dynamic', foreign_keys = 'Penalty.match_id')

    def __init__(self, match_date, home_team_id, away_team_id):
        self.match_date = match_date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.home_team_score = 0
        self.away_team_score = 0

    @staticmethod
    def all_matches():
        stmt = text("SELECT match.id, match.match_date, team.name Home, a.name Away, match.home_team_score, match.away_team_score FROM match JOIN team ON match.home_team_id = team.id JOIN team a ON match.away_team_id = a.id")
        res = db.engine.execute(stmt)
        
        response = []
 
        for row in res:
            # str_date = datetime.datetime(row[0]).strftime("%Y-%m-%d")
            response.append({"id": row[0], "match_date": str(row[1])[:10], "home_team_name": row[2], "away_team_name": row[3], "home_team_score": row[4], "away_team_score": row[5]})

        return response
