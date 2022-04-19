from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("user_create.html")


@app.route('/user_list')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_list.html",user=User.get_by_id(data))


bcrypt = Bcrypt(app)
@app.route('/create', methods=['POST'])
def create_users():
    valid = User.is_valid(request.form)

    if not valid:
        return redirect("/")
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
    return redirect('/user_list')

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
    return redirect('/user_list')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')