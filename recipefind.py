# recipefind.py

from app import app, db_session_scope
from forms import RecipeSearchForm
from flask import render_template, request, redirect, flash
from models import Recipe, Ingredient


@app.route("/", methods=["GET", "POST"])
def index():
    searchform = RecipeSearchForm(request.form)
    if request.method == "POST":
        search_type = ""
        search_term = ""
        results = []
        for item in searchform.data:
            if item.startswith("select"):
                search_type = searchform.data[item]
            elif item.startswith("search"):
                search_term = searchform.data[item]
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
                if results == []:
                    results = query.all()
                else:
                    results = list(set(results) & set(query.all()))
        results = sorted(results, key=lambda x: x.name)

        if results != []:
            flash(f"{len(results)} recipes found!")
            return render_template("index.html", form=searchform, recipes=results)

        # results = []
        # if search1 != "":
        #     query = Recipe.query.filter(Recipe.category.ilike(f"%{search1}%"))
        #     num_found = query.count()
        #     results = query.all()
        #     flash(f"{num_found} recipes found!")
        #     return render_template("index.html", form=searchform, recipes=results)

    return render_template("index.html", title="RecipeFind", form=searchform)


if __name__ == "__main__":
    app.run()


# def find_recipe_by_spirit(spirit_name):
#     r = (
#         Recipe.query.join(Ingredient.recipes)
#         .filter(Ingredient.category.ilike(f"%{spirit_name}%"))
#         .all()
#     )
#     if r is None:
#         print(f"No recipe found for spirit {spirit_name}")
#     else:
#         print(f"Found {len(r)} recipes!")
#         return r
