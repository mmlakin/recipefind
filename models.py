from database import db

ingredient_recipe = db.Table(
    "ingredient_recipe",
    db.Column("ingredient_id", db.ForeignKey("ingredient.id"), primary_key=True),
    db.Column("recipe_id", db.ForeignKey("recipe.id"), primary_key=True),
)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    # recipes = db.relationship(
    #     "Recipe", secondary="ingredient_recipe", backref="ingredients"
    # )

    def __repr__(self):
        return f"Ingredient(name='{self.name}', category='{self.category}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    page_num = db.Column(db.Integer)
    directions = db.Column(db.String)
    notes = db.Column(db.String)
    garnish = db.Column(db.String)
    ingredients = db.relationship(
        "Ingredient", secondary="ingredient_recipe", backref="recipes"
    )

    def __repr__(self):
        return (
            f"{self.name} ({self.category}, page {self.page_num})"
            + "\n\n"
            + "\n".join(
                " ".join(word.capitalize() for word in ingredient.name.split())
                for ingredient in self.ingredients
            )
            + "\n\n"
            + f"{self.directions}\n"
            + f"\n{self.notes}"
        )
