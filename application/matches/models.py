from application import db
from sqlalchemy.sql import text
from application.models import Base


class Match(Base):

    __tablename__ = "match"

    match_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    team = db.relationship("Team", backref='match', lazy=True)

    def __init__(self, match_date, home_team_id, away_team_id):
        self.match_date = match_date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        