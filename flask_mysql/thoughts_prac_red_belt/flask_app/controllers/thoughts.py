from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.thought import Thought


@app.route('/new')
def index1():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_thought.html")

# @app.route("/thought_list")
# def allThoughts():
#     print("test")
#     thoughts = Thought.get_all_thoughts()
#     return render_template("thought_list.html", thoughts=thoughts)

@app.route('/create_thought', methods=["POST"])
def create_thought():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    rValid = Thought.thought_is_valid(request.form)
    if not rValid:
        return redirect("/thought_list")
    data = {
        'thought': request.form['thought'],
        'likes': 1,
        'user_id':session['user_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Thought.saveThought(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/thought_list')

@app.route("/one_thought/<int:id>")
def oneThought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("one_thought.html",thought=Thought.get_one_thought(data))


@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit_thought.html", thought = Thought.get_one_thought(data))

@app.route("/update", methods=['POST'])
def update():
    rValid = Thought.thought_is_valid(request.form)
    if not rValid:
        return redirect(f"/edit/{request.form['id']}")
    Thought.update(request.form)
    return redirect("/thought_list")

@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Thought.update(data)
    return redirect('/thought_list')


@app.route("/like/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Thought.like(data)
    return redirect('/thought_list')