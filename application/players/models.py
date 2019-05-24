from application import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    number = db.Column(db.Integer)
    position = db.Column(db.String(4), nullable=False)

    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
