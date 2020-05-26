from setuptools import setup

with open("README.md") as f:
    readme = f.read()


setup(
    name="RecipeFind",
    version="1.0",
    url="https://github.com/mmlakin/recipefind",
    license="MIT",
    author="Matt Lakin",
    description="Finds recipes based on ingredients, categories, etc.",
    long_description=readme,
    include_package_data=True,
    install_requires=["Flask", "Flask-SQLAlchemy", "Flask-WTF", "python-dotenv"],
)
