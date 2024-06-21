from flask import (
  Blueprint, request
)

blog_bp = Blueprint("blogs", __name__, url_prefix="/blogs")

@blog_bp.route("/")
def get_all_blogs():
  return "Getting all blog posts"


@blog_bp.route("/<int:blog_id>/") # adding converters. read-more here https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
def blog_route(blog_id): # if you pass a string here. it'll fail
  return f"blog_id is {blog_id}"
