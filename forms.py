# forms.py

from wtforms import Form, StringField, SelectField, BooleanField


class RecipeSearchForm(Form):
    options = [
        ("ingredient_name", "Ingredient Name"),
        ("ingredient_category", "Ingredient Category"),
        ("recipe_name", "Recipe Name"),
        ("recipe_category", "Recipe Category"),
        ("recipe_directions", "Recipe Directions"),
        ("recipe_notes", "Recipe Notes"),
    ]
    search1 = StringField("")
    select1 = SelectField("", choices=options)
    exclude1 = BooleanField("Exclude")

    search2 = StringField("")
    select2 = SelectField("", choices=options)
    exclude2 = BooleanField("Exclude")

    search3 = StringField("")
    select3 = SelectField("", choices=options)
    exclude3 = BooleanField("Exclude")

    search4 = StringField("")
    select4 = SelectField("", choices=options)
    exclude4 = BooleanField("Exclude")

    search5 = StringField("")
    select5 = SelectField("", choices=options)
    exclude5 = BooleanField("Exclude")

    search6 = StringField("")
    select6 = SelectField("", choices=options)
    exclude6 = BooleanField("Exclude")

    search7 = StringField("")
    select7 = SelectField("", choices=options)
    exclude7 = BooleanField("Exclude")

    search8 = StringField("")
    select8 = SelectField("", choices=options)
    exclude8 = BooleanField("Exclude")
