from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.employee import Employee
from flask_app.models.form import Form
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
    return render_template("employee_create.html")



@app.route('/dashboard')
def dashboard():
    if 'employee_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['employee_id']
    }
    forms = Form.get_all_with_employee()
    return render_template("dashboard.html",employee=Employee.get_by_all(data), forms=forms)

    



bcrypt = Bcrypt(app)
@app.route('/create', methods=['POST'])
def create_employees():
    valid = Employee.is_valid(request.form)

    if not valid:
        return redirect("/")
    new_employee = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = Employee.save(new_employee)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['employee_id'] = request.form['employee_id']
    session['first_name'] = request.form['first_name']
    return redirect('/dashboard')

bcrypt = Bcrypt(app)
@app.route('/login',methods=['POST'])
def login():
    employee = Employee.get_by_email(request.form)

    if not employee:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(employee.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['employee_id'] = employee.id
    session['first_name'] = employee.first_name
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/update", methods=['POST'])
def update():
    rValid = Employee.employee_is_valid(request.form)
    if not rValid:
        return redirect(f"/edit/{request.form['id']}")
    print(request.form)
    Employee.update(request.form)
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit(id):
    if 'employee_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit.html", employee = Employee.getEmployees(data))



