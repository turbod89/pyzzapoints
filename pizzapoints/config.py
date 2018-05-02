import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://dtorres:sqlpass@localhost/pizzapoints'
    SQLALCHEMY_TRACK_MODIFICATIONS = False