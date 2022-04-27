from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.desk import Desk
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def registration():
    return render_template("registration.html")



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    # desks = Desk.get_all_with_user()
    return render_template("dashboard.html",user=User.get_by_all(data))
# , desks=desks
    



bcrypt = Bcrypt(app)
@app.route('/create', methods=['POST'])
def create_users():
    valid = User.is_valid(request.form)

    if not valid:
        return redirect("/register")
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(new_user)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    session['first_name'] = request.form['first_name']
    return redirect('/dashboard')

bcrypt = Bcrypt(app)
@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/update", methods=['POST'])
def update():
    rValid = User.user_is_valid(request.form)
    if not rValid:
        return redirect(f"/edit/{request.form['id']}")
    print(request.form)
    User.update(request.form)
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit.html", user = User.getUsers(data))



