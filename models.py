# models.py

from app import db

ingredient_recipe = db.Table(
    "ingredient_recipe",
    db.Column("ingredient_id", db.ForeignKey("ingredient.id"), primary_key=True),
    db.Column("recipe_id", db.ForeignKey("recipe.id"), primary_key=True),
)


class Rating(db.Model):
    __bind_key__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    score = db.Column(db.Integer)
    notes = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    recipe = db.relationship("Recipe", back_populates="rating")

    def __repr__(self):
        return (
            f"Rating(name='{self.name}', "
            + f"score='{self.score}', "
            + f"notes='{self.notes}')"
        )


class Stock(db.Model):
    __bind_key__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    ingredient = db.relationship("Ingredient", back_populates="stock")

    def __repr__(self):
        return f"Stock(name='{self.name}', score='{self.statuss}'"


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    stock = db.relationship("Stock", back_populates="ingredient", uselist=False)

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
    rating = db.relationship("Rating", back_populates="recipe", uselist=False)

    def __repr__(self):
        return (
            f"{self.name} ({self.category}, page {self.page_num})"
            + "\n\n"
            + "\n".join(ingredient.name for ingredient in self.ingredients)
            + "\n\n"
            + f"{self.directions}\n"
            + f"\n{self.notes}"
        )
