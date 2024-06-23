# from uuid import uuid4 as v4

# from flask_sqlalchemy import SQLAlchemy # checkout the sql_alchemy docs https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/

# from app import ( # app is referencing the app/ dir
#   app # referencing app initialization in the __init__.py file
# )

# # DATA BASE CONFIGURATION using SQLAlchemy
# db = SQLAlchemy() # this initialization automatically creates the instance folder in app

# # configure the SQLite database, relative to the app instance folder
# # note that this uses a file in the same folder as app. "project.db".
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# # initialize the app with the extension
# db.init_app(app)

# # Creating models
# class UserModel(db.Model):
#   id = db.Column(db.String, primary_key=True)
#   name = db.Column(db.String, nullable=False)
#   email = db.Column(db.String, unique=True, nullable=False)

#   def __init__(this, name: str, email: str):
#     this.id = str(v4()) # ensuring the id is a uuid
#     this.name = name
#     this.email = email
  
#   def getKeys(this):
#     return ["Id", "Name", "Email"]

# with app.app_context():
#   db.create_all() # to create all database models in the instance folder in app
