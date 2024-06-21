# # this file is will run automatically
# print("Hello from __init__ file")

from flask import Flask

from app.blueprints import ( # app.blueprints is referencing the blueprints folder
  index, # this is the index file
  users, # the users file
  blogs,
)

app = Flask(__name__)

app.register_blueprint(index.index_bp)

app.register_blueprint(users.user_bp)

app.register_blueprint(blogs.blog_bp)
