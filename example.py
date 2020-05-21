from models import Recipe, Ingredient


def find_recipe(recipe_name):
    r = Recipe.query.filter(Recipe.name.ilike(f"%{recipe_name}%")).all()
    if r is None:
        print(f"No recipe found for search term {recipe_name}")
    else:
        print(f"Found {len(r)} recipes!")
        return r


def find_recipe_by_spirit(spirit_name):
    r = (
        Recipe.query.join(Ingredient.recipes)
        .filter(Ingredient.category.ilike(f"%{spirit_name}%"))
        .all()
    )
    if r is None:
        print(f"No recipe found for spirit {spirit_name}")
    else:
        print(f"Found {len(r)} recipes!")
        return r


def find_ingredient(ingredient_name):
    i = Ingredient.query.filter(Ingredient.name.ilike(f"%{ingredient_name}%")).all()
    if i is None:
        print(f"No ingredient found for search term {ingredient_name}")
    else:
        print(f"Found {len(i)} ingredients!")
        return i
