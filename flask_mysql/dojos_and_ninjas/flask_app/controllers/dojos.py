from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route("/")
def allDojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route("/newninja")
def newninjapg():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
    } 
    # We pass the data dictionary into the save method from the Friend class.
    Dojo.saveDojo(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')



@app.route("/dojo_show/<int:id>")
def oneDojo(id):
    data ={ 
        "id":id
    }
    return render_template("dojo_show.html",dojo=Dojo.getNinjas(data))