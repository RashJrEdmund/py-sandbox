"""
  This file has everything to do with the users route
"""
from flask import (
  Blueprint, request, render_template
)

user_bp = Blueprint("users", __name__, url_prefix="/users")

template_dir = "users"

@user_bp.route("/") # default methods +=>  methods=["GET"]
def get_all_users():
  return render_template(f"{template_dir}/all.html")

@user_bp.route("/create/")
def create_user_page():
  return render_template(f"{template_dir}/create.html")

@user_bp.route("/<user_name>/") # matching "/users/<user_name>/"
def user_route(user_name):
  return render_template(f"{template_dir}/get-one.html", user_name=user_name)

@user_bp.route("/", methods=["POST"])
def add_user():
  method = request.method
  # json = request.get_json(force=True)
  # print("\n json", json, "\n")

  return f"creating user: method: {method}, name: json.name"
