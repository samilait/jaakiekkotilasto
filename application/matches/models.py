from application import db
from sqlalchemy.sql import text
from application.models import Base
import datetime


class Match(Base):

    __tablename__ = "match"

    match_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    # home_team = db.relationship("Team", backref='match', lazy=True)
    # away_team = db.relationship("Team", backref='match', lazy=True)

    def __init__(self, match_date, home_team_id, away_team_id):
        self.match_date = match_date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id

    @staticmethod
    def all_matches():
        stmt = text("SELECT match.match_date, team.name Home, a.name Away FROM match JOIN team ON match.home_team_id = team.id JOIN team a ON match.away_team_id = a.id")
        res = db.engine.execute(stmt)
        
        response = []

        for row in res:
            # str_date = datetime.datetime(row[0]).strftime("%Y-%m-%d")
            response.append({"match_date": str(row[0])[:10], "home_team_name": row[1], "away_team_name": row[2]})

        return response
