from application import db
from sqlalchemy.sql import text
from application.models import Base
import datetime


class Match(Base):

    __tablename__ = "match"

    match_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    match_goal = db.relationship('Goal', backref = 'match_goal', lazy = 'dynamic', foreign_keys = 'Goal.match_id')

    def __init__(self, match_date, home_team_id, away_team_id):
        self.match_date = match_date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id

    @staticmethod
    def all_matches():
        stmt = text("SELECT match.id, match.match_date, team.name Home, a.name Away FROM match JOIN team ON match.home_team_id = team.id JOIN team a ON match.away_team_id = a.id")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            # str_date = datetime.datetime(row[0]).strftime("%Y-%m-%d")
            response.append({"id": row[0], "match_date": str(row[1])[:10], "home_team_name": row[2], "away_team_name": row[3]})

        return response
