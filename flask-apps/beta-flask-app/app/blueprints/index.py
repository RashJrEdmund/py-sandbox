"""
  This file has everything to do with the index route
"""
from flask import (
  Blueprint, render_template
)

# see docs
# https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route("/")
def index():
  return render_template("index.html")
