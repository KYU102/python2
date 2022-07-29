from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.form import Form
from flask_app.models.employee import Employee


@app.route('/new')
def index12():
    if 'employee_id' not in session:
        return redirect('/logout')
    return render_template("new_form.html")

# @app.route("/dashboard")
# def allForms():
#     print("test")
#     forms = Form.get_all_forms()
#     return render_template("form_list.html", forms=forms)

@app.route('/create_form', methods=["POST"])
def create_form():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    rValid = Form.form_is_valid(request.form)
    if not rValid:
        return redirect("/new")
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'employee_id':session['employee_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Form.saveForm(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')

@app.route("/show/<int:id>")
def oneForm(id):
    if 'employee_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("show.html", form=Form.get_one_form(data))
    # , employee=Employee.get_by_id(data)


# @app.route("/edit/<int:id>")
# def edit(id):
#     if 'employee_id' not in session:
#         return redirect('/logout')
#     data ={
#         "id" : id
#     }
#     return render_template("edit_form.html", form = Form.get_one_form(data))

# @app.route("/update", methods=['POST'])
# def update():
#     rValid = Form.form_is_valid(request.form)
#     if not rValid:
#         return redirect(f"/edit/{request.form['id']}")
#     print(request.form)
#     Form.update(request.form)
#     return redirect("/form_list")

@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Form.delete(data)
    return redirect('/dashboard')

@app.route("/edit/<int:id>")
def edit2(id):
    if 'employee_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit.html", employee = Employee.getMagezines(data))