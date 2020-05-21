#!/usr/bin/env python3

"""
 csvtodb.py

 Parses a CSV file and writes data to a database.

"""

import sys
import csv
from database import init_db
from database import session_scope
from models import Ingredient, Recipe


def parse_csv_recipes(csv_filename: str) -> list:
    RECIPE_NAME = 1
    INGREDIENT_NAME = 2
    INGREDIENT_CATEGORY = 4
    PAGE_NUM = 5
    DIRECTIONS = 6
    NOTES = 7

    recipe_category, recipe_name = None, None

    with open(csv_filename) as f:
        for line in csv.reader(f):
            if (line[RECIPE_NAME], line[DIRECTIONS], line[NOTES]) == ("", "", ""):
                # If all expected columns are blank, skip line
                continue
            if line[RECIPE_NAME] != "" and line[INGREDIENT_NAME] == "":
                # If there's a name and no ingredient, it's a new category
                recipe_category = line[RECIPE_NAME]
                continue

            if line[RECIPE_NAME] != "":
                if line[RECIPE_NAME] != recipe_name:
                    # Create new recipe
                    if recipe_name is not None:
                        # Yield existing recipe first
                        recipe = (
                            recipe_category,
                            recipe_name,
                            recipe_ingredients,
                            recipe_page_num,
                            recipe_garnish,
                            recipe_directions,
                            recipe_notes,
                        )
                        yield recipe
                    # Create/Reset recipe variables
                    recipe_name = line[RECIPE_NAME]
                    recipe_ingredients = list()
                    recipe_page_num = None
                    recipe_directions, recipe_notes, recipe_garnish = "", "", ""

            if line[INGREDIENT_NAME] != "":
                new_ingredient = (line[INGREDIENT_NAME], line[INGREDIENT_CATEGORY])
                if new_ingredient not in recipe_ingredients:
                    # Add ingredient if it's not already in the ingredient list
                    recipe_ingredients.append(new_ingredient)

            if recipe_page_num is None:
                # Set page number
                recipe_page_num = line[PAGE_NUM]

            if line[DIRECTIONS] != "":
                line_directions = line[DIRECTIONS]
                if line_directions.startswith("GARNISH:"):
                    # Set garnish
                    line_directions = line_directions.replace("GARNISH:", "")
                    line_directions = line_directions.replace(",", "")
                    recipe_garnish = line_directions.strip()
                elif line_directions.isupper():
                    # Garnish continues, append
                    recipe_garnish += " " + line_directions
                else:
                    # Set or append to directions
                    if recipe_directions != "":
                        recipe_directions += " "
                    line_directions = line_directions.replace("1,", "1")
                    line_directions = line_directions.strip()
                    recipe_directions += line_directions

            # Set notes
            if line[NOTES] != "":
                if recipe_notes != "":
                    if recipe_notes.isupper():
                        # Add newline after AUTHOR YEAR note header
                        recipe_notes += "\n"
                    else:
                        recipe_notes += " "
                recipe_notes += line[NOTES]

    recipe = (
        recipe_category,
        recipe_name,
        recipe_ingredients,
        recipe_page_num,
        recipe_garnish,
        recipe_directions,
        recipe_notes,
    )
    yield recipe


def populate_db_recipes(recipe_list: iter) -> None:
    CATEGORY = 0
    NAME = 1
    INGREDIENTS = 2
    PAGE_NUM = 3
    GARNISH = 4
    DIRECTIONS = 5
    NOTES = 6
    with session_scope() as session:
        for item in recipe_list:
            ingredient_list = []
            for ingredient_name, ingredient_category in item[INGREDIENTS]:
                ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
                if ingredient is None:
                    ingredient = Ingredient(
                        name=ingredient_name, category=ingredient_category
                    )
                ingredient_list.append(ingredient)
            session.add(
                Recipe(
                    category=item[CATEGORY],
                    name=item[NAME],
                    ingredients=ingredient_list,
                    page_num=item[PAGE_NUM],
                    garnish=item[GARNISH],
                    directions=item[DIRECTIONS],
                    notes=item[NOTES],
                )
            )


def main(csv_filename):
    init_db()
    populate_db_recipes(parse_csv_recipes(csv_filename))


def print_usage():
    print(
        "csvtodb.py - Convert CSV to DB file\n",
        "Usage: python3 csvtodb.py input.csv output.db",
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        quit()

    main(sys.argv[1])
