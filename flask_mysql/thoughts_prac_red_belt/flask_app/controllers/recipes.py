from flask import render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe


@app.route('/new')
def index1():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_recipe.html")

# @app.route("/recipe_list")
# def allRecipes():
#     print("test")
#     recipes = Recipe.get_all_recipes()
#     return render_template("recipe_list.html", recipes=recipes)

@app.route('/create_recipe', methods=["POST"])
def create_recipe():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    rValid = Recipe.recipe_is_valid(request.form)
    if not rValid:
        return redirect("/new")
    data = {
        'name': request.form['name'],
        'under30': request.form['under30'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id':session['user_id']
    }
    # We pass the data dictionary into the save method from the Friend class.
    Recipe.saveRecipe(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/recipe_list')

@app.route("/one_recipe/<int:id>")
def oneRecipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("one_recipe.html",recipe=Recipe.get_one_recipe(data))


@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id" : id
    }
    return render_template("edit_recipe.html", recipe = Recipe.get_one_recipe(data))

@app.route("/update", methods=['POST'])
def update():
    rValid = Recipe.recipe_is_valid(request.form)
    if not rValid:
        return redirect(f"/edit/{request.form['id']}")
    print(request.form)
    Recipe.update(request.form)
    return redirect("/recipe_list")

@app.route("/delete/<int:id>")
def delete(id):
    data ={
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/recipe_list')