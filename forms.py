# forms.py

from wtforms import Form
from wtforms import StringField, SelectField, BooleanField
from wtforms import TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import InputRequired, DataRequired, Length
from flask_wtf import FlaskForm


class RecipeFilterForm(FlaskForm):
    ing_name = StringField("Include Ingredients")
    x_ing_name = StringField("Exclude Ingredients")
    ing_cat = StringField("Include Ingredient Categories")
    x_ing_cat = StringField("Exclude Ingredient Categories")
    rec_cat = StringField("Include Recipe Categories")
    x_rec_cat = StringField("Exclude Recipe Categories")
    rec_name = StringField("Include Recipe Name")
    x_rec_name = StringField("Exclude Recipe Name")
    rec_dir = StringField("Include Recipe Directions")
    x_rec_dir = StringField("Exclude Recipe Directions")
    rec_note = StringField("Include Recipe Notes")
    x_rec_note = StringField("Exclude Recipe Notes")
    submit = SubmitField("Search Recipes")


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


class NewItemForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            InputRequired("Input is required!"),
            DataRequired("Valid title required"),
            Length(min=5, max=20, message="Must be between 5 and 20 characters long"),
        ],
    )
    description = TextAreaField(
        "Description",
        validators=[
            InputRequired("Input is required!"),
            DataRequired("Valid description required"),
            Length(min=5, max=40, message="Must be between 5 and 20 characters long"),
        ],
    )
    category = SelectMultipleField("Category")
    submit = SubmitField("Submit")
