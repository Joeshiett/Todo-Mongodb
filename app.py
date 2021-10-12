from flask import Flask, url_for, redirect, request
from flask.templating import render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(
    os.environ['TODO_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb


@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)

@app.route('/new', methods=["POST"])
def new():

    item_doc = {
        "name": request.form['name'],
        "description": request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")