from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.magazine import Magazine
from flask_app.models.user import User


@app.route('/new')
def index12():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_magazine.html")

# @app.route("/dashboard")
# def allMagazines():
#     print("test")
#     magazines = Magazine.get_all_magazines()
#     return render_template("magazine_list.html", magazines=magazines)

@app.route('/create_magazine', methods=["POST"])
def create_magazine():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    rValid = Magazine.magazine_is_valid(request.form)
    if not rValid:
        return redirect("/new")
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id':session['user_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Magazine.saveMagazine(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')

@app.route("/show/<int:id>")
def oneMagazine(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("show.html", magazine=Magazine.get_one_magazine(data))
    # , user=User.get_by_id(data)


# @app.route("/edit/<int:id>")
# def edit(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         "id" : id
#     }
#     return render_template("edit_magazine.html", magazine = Magazine.get_one_magazine(data))

# @app.route("/update", methods=['POST'])
# def update():
#     rValid = Magazine.magazine_is_valid(request.form)
#     if not rValid:
#         return redirect(f"/edit/{request.form['id']}")
#     print(request.form)
#     Magazine.update(request.form)
#     return redirect("/magazine_list")

@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Magazine.delete(data)
    return redirect('/dashboard')

@app.route("/edit/<int:id>")
def edit2(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit.html", user = User.getMagezines(data))