# recipefind.py
import pdb
from flask import render_template, request, flash, redirect, url_for
from app import app, db
from models import Recipe, Ingredient
from forms import RecipeFilterForm, RecipeSearchForm, NewItemForm


@app.route("/searchtest", methods=["GET", "POST"])
def test():
    # TESTING Bootstrap searchable multi-select box
    items = [item[0] for item in db.session.query(Recipe.category.distinct()).all()]
    return render_template("searchtest.html", items=items)


@app.route("/home", methods=["GET", "POST"])
def home():
    # New site - working
    recipes = Recipe.query.all()
    form = RecipeFilterForm(request.args, meta={"csrf": False})
    if form.validate():
        queries = []
        for field in form:
            if field.type != "SubmitField":
                if field.data.strip():
                    exclude = False
                    if field.name.startswith("x_"):
                        exclude = True
                    if field.name.count("ing_"):
                        query = Recipe.query.join(Recipe.ingredients)
                        q_filter = Ingredient
                    elif field.name.count("rec_"):
                        query = Recipe.query
                        q_filter = Recipe
                    if field.name.endswith("_name"):
                        q_filter = q_filter.name.ilike
                    elif field.name.endswith("_cat"):
                        q_filter = q_filter.category.ilike
                    elif field.name.endswith("_dir"):
                        q_filter = q_filter.directions.ilike
                    elif field.name.endswith("_note"):
                        q_filter = q_filter.notes.ilike

                    for item in field.data.split(","):
                        queries.append((query, q_filter(f"%{item.strip()}%"), exclude,))

        for q, f, e in queries:
            if e:
                recipes = list(set(recipes).difference(set(q.filter(f).all())))
            else:
                recipes = list(set(recipes) & set(q.filter(f).all()))
        recipes = sorted(recipes, key=lambda x: x.name)

        flash(f"{len(recipes)} recipes found!", "success")
        return render_template("home.html", form=form, recipes=recipes)

    return render_template("home.html", form=form, recipes=recipes)


@app.route("/recipe/<int:recipe_id>", methods=["GET"])
def recipe(recipe_id):
    try:
        recipe = Recipe.query.filter_by(id=recipe_id).one()
    except:
        recipe = None
    if recipe is not None:
        return render_template("recipe.html", recipe=recipe)
    return redirect(url_for("home"))


@app.route("/ingredient/<int:ingredient_id>", methods=["GET"])
def ingredient(ingredient_id):
    try:
        ingredient = Ingredient.query.filter_by(id=ingredient_id).one()
    except:
        ingredient = None
    if ingredient is not None:
        return render_template("ingredient.html", ingredient=ingredient)
    return redirect(url_for("home"))


@app.route("/item/new", methods=["GET", "POST"])
def new_item():
    # TESTING site for adding new items
    form = NewItemForm()
    recipe_categories = [
        # (item[0], item[0])
        (item[0].replace(" ", "_").lower(), item[0])
        for item in db.session.query(Recipe.category.distinct()).all()
    ]
    form.category.choices = recipe_categories
    if form.validate_on_submit():
        flash(
            "Successfully added new item {}".format(form.title.data), "success",
        )
        return redirect(url_for("home"))
    if form.errors:
        for field in form.errors:
            for err in form.errors[field]:
                flash("ERROR: {} - {}".format(field.title(), err.title()), "danger")
    return render_template("new_item.html", form=form)


@app.route("/", methods=["GET", "POST"])
def index():
    # OLD site - working
    searchform = RecipeSearchForm(request.form)
    if request.method == "POST":
        search_type = ""
        search_term = ""
        results = None
        total_items = 0
        for item in searchform.data:
            if item.startswith("select"):
                search_type = searchform.data[item]
            elif item.startswith("search"):
                search_term = searchform.data[item]
            elif item.startswith("exclude"):
                if search_term == "":
                    continue
                total_items += 1
                exclude = searchform.data[item]
                if search_type == "recipe_category":
                    query = Recipe.query.filter(
                        Recipe.category.ilike(f"%{search_term}%")
                    )
                elif search_type == "recipe_name":
                    query = Recipe.query.filter(Recipe.name.ilike(f"%{search_term}%"))
                elif search_type == "recipe_notes":
                    query = Recipe.query.filter(Recipe.notes.ilike(f"%{search_term}%"))
                elif search_type == "recipe_directions":
                    query = Recipe.query.filter(
                        Recipe.directions.ilike(f"%{search_term}%")
                    )
                elif search_type == "ingredient_category":
                    query = Recipe.query.join(Ingredient.recipes).filter(
                        Ingredient.category.ilike(f"%{search_term}%")
                    )
                elif search_type == "ingredient_name":
                    query = Recipe.query.join(Ingredient.recipes).filter(
                        Ingredient.name.ilike(f"%{search_term}%")
                    )
                if total_items == 1:
                    results = query.all()
                    if exclude is True:
                        # Exclude chosen query from all recipes
                        results = list(set(Recipe.query.all()).difference(set(results)))
                else:
                    newresults = query.all()
                    if exclude is True:
                        results = list(set(results).difference(set(newresults)))
                    else:
                        results = list(set(results) & set(newresults))
        if total_items == 0:
            # Show all recipes
            results = Recipe.query.all()

        results = sorted(results, key=lambda x: x.name)

        pdb.set_trace()
        if results is not None:
            flash(f"{len(results)} recipes found!", "success")
            return render_template("index.html", form=searchform, recipes=results)

    return render_template("index.html", title="RecipeFind", form=searchform)


if __name__ == "__main__":
    app.run()
