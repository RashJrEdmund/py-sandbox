# # this file is will run automatically
# print("Hello from __init__ file")

from flask import Flask
from uuid import uuid4 as v4

from flask_sqlalchemy import SQLAlchemy # checkout the sql_alchemy docs https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/

from app.blueprints import ( # app.blueprints is referencing the blueprints folder in the app/ dir
  index, # this is the index file
  users, # the users file
  blogs,
)

from app.extensions import (
  db
)

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
# note that this uses a file in the same folder as app. "project.db".
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db.init_app(app)

#
# registering blueprints
app.register_blueprint(index.index_bp)

app.register_blueprint(users.user_bp)

app.register_blueprint(blogs.blog_bp)

with app.app_context():
  db.create_all() # to create all database models in the instance folder in app
