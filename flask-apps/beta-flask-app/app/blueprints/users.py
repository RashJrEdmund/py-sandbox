"""
  This file has everything to do with the users route
"""
from flask import (
  Blueprint, render_template,
  request, redirect,
  url_for,
)

from app.extensions import db

from app.models.user import ( # app here is the app folder referencing the __init__ file
  UserModel, # use these docs to know how to query using db.session, https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data
)

user_bp = Blueprint("users", __name__, url_prefix="/users")

template_dir = "users"

@user_bp.route("/") # default methods +=>  methods=["GET"]
def get_all_users():
  users = UserModel.query.all()

  return render_template(f"{template_dir}/all.html", users=users)

@user_bp.route("/create/")
def create_user_page():
  return render_template(f"{template_dir}/create.html")

@user_bp.route("/<uuid:user_id>/") # matching "/users/<user_id>/" an making use of the uuid converter. read more about converters here  https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
def user_route(user_id):
  user = UserModel.query.get(str(user_id))

  return render_template(f"{template_dir}/get-one.html", user=user)

@user_bp.route("/", methods=["POST"])
def add_user():
  #json = request.json # request content type should be application/json first before we can get the json
  method = request.method
  form = request.form

  new_user = UserModel(
    name=form["name"],
    email=form["email"]
  )

  db.session.add(new_user) # saving new user to db
  db.session.commit()

  return redirect(url_for("users.create_user_page"))
  """
    url_for("users.create_user_page") simple means;
    "go to the user blueprint, find a function called 'create_user_page'
    and return it's route". So in this case, it'll return "users/create"

    Since submitting the form in the create_user_page() handler redirects to
    this add_user() handler, I'm using the redirect() function along side the
    url_for("users.create_user_page") to redirect back to the form page.
  """

@user_bp.route("/<uuid:user_id>", methods=["DELETE"]) # making use of the uuid converter
def delete_user(user_id):
  user = UserModel.query.get(str(user_id))

  db.session.delete(user)
  db.session.commit()

  print("\n", user.name, "\n")

  return f"delete user {user_id}"