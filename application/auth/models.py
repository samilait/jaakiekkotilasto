from application import db
from application.models import Base

account_match = db.Table('account_match',
                db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
                db.Column('match_id', db.Integer, db.ForeignKey('match.id'))
)


class User(Base):

    __tablename__ = "account"

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    matches = db.relationship('Match', secondary=account_match, backref=db.backref('match_accounts', lazy='dynamic'))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return ["ADMIN"]
        
