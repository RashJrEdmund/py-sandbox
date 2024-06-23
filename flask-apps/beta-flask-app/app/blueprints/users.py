"""
  This file has everything to do with the users route
"""
from flask import (
  Blueprint, render_template,
  request, redirect,
  url_for,
)

# from app import ( # app here is the app folder referencing the __init__ file
#   UserModel, # use these docs to know how to query using db.session, https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data
# )

user_bp = Blueprint("users", __name__, url_prefix="/users")

template_dir = "users"

@user_bp.route("/") # default methods +=>  methods=["GET"]
def get_all_users():
  from app import UserModel

  users = UserModel.query.all()

  return render_template(f"{template_dir}/all.jinja", users=users)

@user_bp.route("/create/")
def create_user_page():
  return render_template(f"{template_dir}/create.jinja")

@user_bp.route("/<user_name>/") # matching "/users/<user_name>/"
def user_route(user_name):
  return render_template(f"{template_dir}/get-one.jinja", user_name=user_name)

@user_bp.route("/", methods=["POST"])
def add_user():
  #json = request.json # request content type should be application/json first before we can get the json
  method = request.method
  form = request.form

  # return form # sends back, as json, the form

  # store user in db

  return redirect(url_for("users.create_user_page"))
  """
    url_for("users.create_user_page") simple means;
    "go to the user blueprint, find a function called 'create_user_page'
    and return it's route". So in this case, it'll return "users/create"

    Since submitting the form in the create_user_page() handler redirects to
    this add_user() handler, I'm using the redirect() function along side the
    url_for("users.create_user_page") to redirect back to the form page.
  """

  return f"creating user: method: {method}, name: json.name"
