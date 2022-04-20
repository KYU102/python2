from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.thought import Thought
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("user_create.html")


@app.route('/thought_list')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    thoughts = Thought.get_all_thoughts()
    return render_template("thought_list.html",user=User.get_by_id(data), thoughts=thoughts)


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
    session['first_name'] = request.form['first_name']
    return redirect('/thought_list')

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
    return redirect('/thought_list')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')