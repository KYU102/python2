from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.form import Form
from flask_app.models.employee import Employee


@app.route('/new')
def index12():
    if 'employee_id' not in session:
        return redirect('/logout')
    return render_template("new_form.html")

@app.route('/create_form', methods=["POST"])
def create_form():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # rValid = Form.form_is_valid(request.form)
    # if not rValid:
    #     return redirect("/new")
    data = {
        'close_contact': request.form['close_contact'],
        'exposure_date': request.form['exposure_date'],
        'employee_id':session['employee_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Form.saveForm(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'employee_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['employee_id']
    }
    forms = Form.get_all()
    return render_template("dashboard.html",forms=forms)

