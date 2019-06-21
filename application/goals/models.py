from application import db
from sqlalchemy.sql import text
from application.models import Base


class Goal(Base):

    __tablename__ = "goal"

    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)    # Done
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)      # Done
    time = db.Column(db.String(5), nullable=False)
    scorer_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)           # Done
    assistant_1_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)      # Done
    assistant_2_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)      # Done

    def __init__(self, match_id, team_id, time, scorer_id, assistant_1_id, assistant_2_id):
        self.match_id = match_id
        self.team_id = team_id
        self.time = time
        self.scorer_id = scorer_id
        self.assistant_1_id = assistant_1_id
        self.assistant_2_id = assistant_2_id

