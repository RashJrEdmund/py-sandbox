from uuid import uuid4 as v4

from app.extensions import ( # app is referencing the app/ dir then extensions/
  db # referencing app initialization in the __init__.py file
)

# Creating model
class UserModel(db.Model):
  id = db.Column(db.String, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)

  def __init__(this, name: str, email: str):
    this.id = str(v4()) # ensuring the id is a uuid
    this.name = name
    this.email = email
  
  def getKeys(this):
    return ["Id", "Name", "Email"]
