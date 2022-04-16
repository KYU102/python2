from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.dojo import Survey


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create',methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/show')
    return redirect('/')

@app.route('/show')
def results():
    return render_template('show.html', survey = Survey.get_last_survey())

