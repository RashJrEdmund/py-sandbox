from flask import Flask, request

app = Flask(__name__)

# print("\nname is", __name__)

@app.route("/")
def index():
  return "<h1>hello world</h1>"

#
# DYNAMIC ROUTING. GETTING PARAMS
#
@app.route("/user/<user_name>/")
def user_route(user_name):
  return f"Hello {user_name}"

@app.route("/blog/<int:blog_id>/") # adding converters. read-more here https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
def blog_route(blog_id): # if you pass a string here. it'll fail
  return f"blog_id is {blog_id}"

###
###
### Handling other request methods

@app.route("/users/", methods=["POST"])
def create_user():
  method = request.method
  json = request.get_json(force=True)
  print("\n json", json, "\n")

  return f"creating user: method: {method}, name: json.name"

@app.route("/users/", methods=["GET"])
def get_all_users():
  return "getting all user"