from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template("email_create.html")

@app.route('/create',methods=['POST'])
def create_emails():
    if Email.is_valid(request.form):
        Email.save(request.form)
        return redirect('/email_list')
    return redirect('/')

@app.route('/email_list')
def results():
    return render_template('email_list.html', emails = Email.get_all_emails())