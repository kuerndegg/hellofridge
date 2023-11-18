from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json
import os

def load_recipes():
    if os.path.exists('recipes.json'):
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    else:
        recipes = []
    return recipes


app = FastAPI()

# Mock data for recipes
recipes = load_recipes()

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