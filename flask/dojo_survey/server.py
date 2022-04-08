from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['fname'] = request.form['fname']
    session['lang']= request.form['lang']
    session['loc'] = request.form['loc']
    session['com'] = request.form['com']
    return redirect("/show")	 

@app.route('/show')
def display():
    return render_template("show.html")


if __name__=="__main__":
    app.run(debug=True,port=5004)
