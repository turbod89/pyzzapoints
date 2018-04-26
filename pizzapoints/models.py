from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    screenName = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=True)
    secondName = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.screenName