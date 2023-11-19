from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

HOSTURL = "http://localhost:8000"

def load_recipes():
    if os.path.exists('recipes.json'):
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    else:
        recipes = []
    for id, recipe in enumerate(recipes):
        recipe['id'] = id
    return recipes

def load_ingredients():
    if os.path.exists('ingredients.json'):
        with open('ingredients.json', 'r') as file:
            ingredients = json.load(file)
    else:
        ingredients = []
    for ingredient in ingredients:
        ingredient['image'] = f"{HOSTURL}/images/{ingredient['image']}"
    return ingredients

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data for recipes
recipes = load_recipes()
ingredients = load_ingredients()

# Mock data for ingredientss

app.mount("/images", StaticFiles(directory="images"), name="images")

class Ingredient(BaseModel):
    name: str
    category: str
    image: str

class RecipeIngredient(BaseModel):
    item: str
    amount: str

class Recipe(BaseModel):
    id: int
    title: str
    url: str
    image: str
    at_home: int = 0
    tags: Optional[List[str]]
    ingredients: Optional[List[RecipeIngredient]]
    steps: Optional[List[str]]


@app.get("/recipes")
def get_recipes(with_steps: bool = False)->List[Recipe]:
    if not with_steps:
        rcps = []
        for recipe in recipes:
            recipe['steps'].clear()
            rcps.append(recipe)
        return rcps
    else:
        return recipes

@app.get("/recipe/{id}")
def get_recipe(id: int)->Recipe:
    return recipes[id]

@app.get("/ingredients")
def get_ingredients()->List[Ingredient]:
    return ingredients

@app.post("/recipes")
def get_recipes_by_ingredients(ingredients: List[str])->List[Recipe]:
    recipes_by_ingredients = recipes.copy()
    for recipe in recipes_by_ingredients:
        recipe['at_home'] = 0
        for ingredient in recipe['ingredients']:
            if ingredient['item'] in ingredients:
                recipe['at_home'] += 1
    # sort by number of ingredients at home
    for i in range(len(recipes_by_ingredients)):
        for j in range(i+1, len(recipes_by_ingredients)):
            if recipes_by_ingredients[i]['at_home'] < recipes_by_ingredients[j]['at_home']:
                recipes_by_ingredients[i], recipes_by_ingredients[j] = recipes_by_ingredients[j], recipes_by_ingredients[i]
    return recipes_by_ingredients