from flask import Flask, jsonify
from flask_cors import CORS
store = []

app = Flask(__name__)
CORS(app)
from flask import request

# receive request for new public id
@app.route('/add', methods=['GET'])
def add_public_id():
    args = request.args
    store.append(args["public_id"])
    return "ok"

# list all public ids
@app.route("/list")
def list_public_ids():
  return jsonify(store)


#localhost:5000/list - displays public_id of images uploaded
#localhost:5000/add - adds new public_id ('http://localhost:5000/add?public_id=...)
#localhost:8000 - widget, display of images added