from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.desk import Desk
from flask_app.models.user import User
from flask_app.models.perf import Peripheral

@app.route('/new/perf')
def newPerf():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_perf.html")


@app.route('/create_perf', methods=["POST"])
def create_perf():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # rValid = Desk.desk_is_valid(request.form)
    # if not rValid:
    #     return redirect("/new")
    data = {
        'name': request.form['name'],
        'link': request.form['link'],
        'price': request.form['price'],
        'theme': request.form['theme']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Peripheral.savePerf(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')