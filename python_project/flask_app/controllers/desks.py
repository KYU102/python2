from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.desk import Desk
from flask_app.models.user import User
from flask_app.models.perf import Peripheral


@app.route('/new')
def index12():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_desk.html")

# @app.route("/dashboard")
# def allDesks():
#     print("test")
#     desks = Desk.get_all_desks()
#     return render_template("desk_list.html", desks=desks)

@app.route('/create_desk', methods=["POST"])
def create_desk():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    rValid = Desk.desk_is_valid(request.form)
    if not rValid:
        return redirect("/new")
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id':session['user_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Desk.saveDesk(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/new/perf')

@app.route("/show/<int:id>")
def oneDesk(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("show.html", desk=Desk.get_one_desk(data))
    # , user=User.get_by_id(data)


# @app.route("/edit/<int:id>")
# def edit(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         "id" : id
#     }
#     return render_template("edit_desk.html", desk = Desk.get_one_desk(data))

# @app.route("/update", methods=['POST'])
# def update():
#     rValid = Desk.desk_is_valid(request.form)
#     if not rValid:
#         return redirect(f"/edit/{request.form['id']}")
#     print(request.form)
#     Desk.update(request.form)
#     return redirect("/desk_list")

@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Desk.delete(data)
    return redirect('/dashboard')

@app.route("/edit/<int:id>")
def edit2(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit.html", user = User.getMagezines(data))