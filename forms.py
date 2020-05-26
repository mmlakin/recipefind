# forms.py

from wtforms import Form, StringField, SelectField


class RecipeSearchForm(Form):
    options = [
        ("ingredient_name", "Ingredient Name"),
        ("ingredient_category", "Ingredient Category"),
        ("recipe_name", "Recipe Name"),
        ("recipe_category", "Recipe Category"),
    ]
    select1 = SelectField("Filter 1", choices=options)
    search1 = StringField("")

    select2 = SelectField("Filter 2", choices=options)
    search2 = StringField("")

    select3 = SelectField("Filter 3", choices=options)
    search3 = StringField("")

    select4 = SelectField("Filter 4", choices=options)
    search4 = StringField("")
