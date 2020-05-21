# RecipeFind

WIP - Currently, only the csvtodb.py is working to create the sqlite db

This app will provide a simple UI for finding a recipe based on different filters like ingredients, categories, etc.

It will also serve as my initial foray into working with databases and web frameworks, so here's to learning!


## Usage

First, clone the repository, create & activate a virtualenv, and install the requirements:

```
git clone https://github.com/mmlakin/recipefind.git
cd recipefind
python3 -m venv ./.venv
. ./.venv/bin/activate
pip install -r requirements.txt
```
Then, bootstrap the database:

`$ python3 csvtodb.py deathco-recipes.csv`

That's about it for now.  You can use some basic queries via shell:

`sqlite3 test.db 'SELECT * FROM ingredients'`

To start seeing the database entries and relationships, check out example.py:

`$ python3`

```
>>> import example
>>> r = example.find_recipe('manhat')
Found 3 recipes!
>>> r[0].name
'MANHATTAN'
>>> r[0]
MANHATTAN (CLASSIC AND VINTAGE, page 145)

Rittenhouse 100 Rye
House Sweet Vermouth
Angostura Bitters

Stir all the ingredients over ice, then strain into a coupe. Garnish with the cherry.

>>> r = example.find_recipe_by_spirit('whiskey')
Found 115 recipes!
>>> len(r)
115
>>> r[0].name
'BLOOD AND SAND'
```

...and so on.
