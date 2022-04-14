
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/")
def allUsers():
    users = User.get_all()
    return render_template("read(all).html", users=users)



@app.route("/add")
def newUser():
    return render_template("create.html",users=User.get_all())



@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

@app.route("/read(one)/<int:id>")
def oneUser(id):
    data ={ 
        "id":id
    }
    return render_template("read(one).html",user=User.get_one(data))




@app.route("/edit/<int:id>")
def edit(id):
    data ={
        "id" : id
    }
    return render_template("edit.html", user = User.get_one(data))



@app.route("/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect(f"/read(one)/{request.form['id']}")





@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    User.delete(data)
    return redirect('/')