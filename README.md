# RecipeFind

This app will provide a simple UI for finding a recipe based on different filters like ingredients, categories, etc.

It will also serve as my initial foray into working with databases and web frameworks, so here's to learning!


This is a work in progress.

Currently there are 8 manual filters and an exclude option.

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

`python3 csvtodb.py deathco-recipes.csv`

Finally, start the Flask app:

`flask run`

Navigate to the website, choose the filters you want, and click Search to display the matching recipes.  Continue adding filters to reduce the number of matching recipes displayed.
