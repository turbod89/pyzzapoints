import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import defineModels
from .routes import defineRoutes

app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='thisisasecretkey',
    USERNAME='admin',
    PASSWORD='admin'
))

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dtorres:sqlpass@localhost/pizzapoints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Config)

app.config.from_envvar('PYZZAPOINTS_SETTINGS', silent=True)

with app.app_context():
    db = SQLAlchemy(app)
    g.sqlalchemy_db = db

    defineModels(db)


    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlalchemy_db'):
            g.sqlalchemy_db.session.close()

    """
        Commands
    """

    @app.cli.command('initdb')
    def initdb_command():
        """Initializes the database."""
        db.create_all()
        db.session.commit()


    """
        Routes
    """


    defineRoutes(app,db)