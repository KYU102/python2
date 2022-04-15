from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    } 
    # We pass the data dictionary into the save method from the Friend class.
    Ninja.saveNinja(data)
    print(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

    