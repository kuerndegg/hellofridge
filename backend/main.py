from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mock data for recipes
recipes = [
    {"id": 1, "title": "Pasta Carbonara", "description": "Delicious pasta dish"},
    {"id": 2, "title": "Chicken Curry", "description": "Spicy chicken curry"},
    # Add more recipes here
]

# Mock data for ingredients
ingredients = [
    {"id": 1, "name": "Tomato", "category": "Vegetables", "image": "tomato.jpg"},
    {"id": 2, "name": "Chicken", "category": "Meat", "image": "chicken.jpg"},
    # Add more ingredients here
]

app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/recipes")
def get_recipes():
    return recipes

@app.get("/ingredients")
def get_ingredients():
    return ingredients