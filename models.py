from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Text, ForeignKey
from sqlalchemy.orm import relationship

ingredients_recipes = Table(
    "ingredients_recipes",
    Base.metadata,
    Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True),
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
)


class Ingredient(Base):
    __tablename__ = "ingredients"

    name = Column(String)
    category = Column(String)
    recipes = relationship(
        "Recipe", secondary="ingredients_recipes", back_populates="ingredients"
    )

    def __repr__(self):
        return f"Ingredient(name='{self.name}', category='{self.category}')"


class Recipe(Base):
    __tablename__ = "recipes"

    name = Column(String)
    category = Column(String)
    page_num = Column(Integer)
    directions = Column(String)
    notes = Column(String)
    garnish = Column(String)
    ingredients = relationship(
        "Ingredient", secondary="ingredients_recipes", back_populates="recipes"
    )

    def __repr__(self):
        return (
            f"Recipe(name='{self.name}', catgeory='{self.category}',"
            + f"page_num='{self.page_num}', directions='{self.directions}',"
            + f"notes='{self.notes}', garnish='{self.garnish}')"
        )
