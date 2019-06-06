from application import db


class Team(db.Model):

    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def __init__(self, name):
        self.name = name
