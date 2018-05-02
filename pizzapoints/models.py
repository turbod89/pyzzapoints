def defineModels(db):
    
    class User(db.Model):

        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        screenName = db.Column(db.String(80), unique=True, nullable=False)
        firstName = db.Column(db.String(80), unique=False, nullable=True)
        secondName = db.Column(db.String(80), unique=False, nullable=True)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.screenName

    class Group(db.Model):

        __tablename__ = 'groups'

        id = db.Column(db.Integer, primary_key=True)
        code = db.Column(db.String(32), unique=True, nullable=False)
        description = db.Column(db.String(128), unique=False, nullable=True)

        def __repr__(self):
            return '<Group %r>' % self.code


    relUsersGroups = db.Table('relUsersGroups',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
        db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    )