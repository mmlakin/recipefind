# RecipeFind

WIP - Currently, only the csvtodb.py is working to create the sqlite db

This app will provide a simple IU for finding a recipe based on different filters like ingredients, categories, etc.


## Usage

First, clone the repository and create a virtualenv. Then install the requirements:

`pip3 install -r requirements.txt`

Then, bootstrap the database:

`$ python3 csvtodb.py deathco-recipes.csv`

That's about it for now.  You can use some basic queries via shell:

`sqlite3 test.db 'SELECT * FROM ingredients'

To start seeing the database entries and relationships, load up python:

`$ python3`

```
>>> from database import Session
from models import Ingredient, Recipe

session = Session()
results = session.query(Recipe).filter(Recipe.name.like('%Manhatt%')).all()
len(results)
results[0]
results[0].ingredients
results[0].ingredients[0]
results[0].ingredients[0].recipes
results[0].ingredients[0].recipes[0]
results[0].ingredients[0].recipes[0].ingredients
```
...and so on.
