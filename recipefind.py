# recipefind.py

from app import app
from forms import RecipeSearchForm
from flask import render_template, request, flash
from models import Recipe, Ingredient


@app.route("/", methods=["GET", "POST"])
def index():
    searchform = RecipeSearchForm(request.form)
    if request.method == "POST":
        search_type = ""
        search_term = ""
        results = None
        for item in searchform.data:
            if item.startswith("select"):
                search_type = searchform.data[item]
            elif item.startswith("search"):
                search_term = searchform.data[item]
            elif item.startswith("exclude"):
                if search_term == "":
                    continue
                exclude = searchform.data[item]
                if search_type == "recipe_category":
                    query = Recipe.query.filter(
                        Recipe.category.ilike(f"%{search_term}%")
                    )
                elif search_type == "recipe_name":
                    query = Recipe.query.filter(Recipe.name.ilike(f"%{search_term}%"))
                elif search_type == "ingredient_category":
                    query = Recipe.query.join(Ingredient.recipes).filter(
                        Ingredient.category.ilike(f"%{search_term}%")
                    )
                elif search_type == "ingredient_name":
                    query = Recipe.query.join(Ingredient.recipes).filter(
                        Ingredient.name.ilike(f"%{search_term}%")
                    )
                if results is None:
                    results = query.all()
                else:
                    newresults = query.all()
                    if exclude is True:
                        results = list(set(results).difference(set(newresults)))
                    else:
                        results = list(set(results) & set(newresults))
        results = sorted(results, key=lambda x: x.name)

        if results is not None:
            flash(f"{len(results)} recipes found!")
            return render_template("index.html", form=searchform, recipes=results)

    return render_template("index.html", title="RecipeFind", form=searchform)


if __name__ == "__main__":
    app.run()
