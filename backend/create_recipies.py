import json
import streamlit as st
import os

def load_recipes():
    if os.path.exists('recipes.json'):
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    else:
        recipes = []
    return recipes

def add_recipe(title, tags, ingredients, steps, url, picture):
    recipe = {
        "title": title,
        "url": url,
        "picture": picture,
        "tags": tags,
        "ingredients": ingredients,
        "steps": steps
    }
    recipes.append(recipe)

def main():
    st.title("Recipe Manager")

    # Load existing recipes
    global recipes
    recipes = load_recipes()

    # Display existing recipes
    st.header("Existing Recipes")
    for recipe in recipes:
         st.write("- " + recipe["title"])
         st.image(recipe['picture'], width=200)
    #     st.write("Tags:", ", ".join(recipe["tags"]))
    #     st.write("Ingredients:")
    #     for ingredient in recipe["ingredients"]:
    #         st.write(f"- {ingredient['item']}: {ingredient['amount']}")
    #     st.write("Steps:")
    #     for i, step in enumerate(recipe["steps"], start=1):
    #         st.write(f"{i}. {step}")
    #     st.write("---")

    # Add a new recipe
    st.header("Add New Recipe")
    title = st.text_input("Title")
    url = st.text_input("Recipe URL")
    picture = st.text_input("Picture URL")
    tags = st.text_input("Tags (•-separated)")
    ingredients = st.text_area("Ingredients (one per line)(split item and amount with a semicolon)",height=400)
    steps = st.text_area("Steps (one per line)")

    if st.button("Add Recipe"):
        tags = [tag.strip() for tag in tags.split("•")]
        ingredients = [{"item": item.strip(), "amount": amount.strip()} for item, amount in
                       [line.split(";", 1) for line in ingredients.split("\n")]]
        steps = [step.strip() for step in steps.split(";\n")]

        add_recipe(title, tags, ingredients, steps, url, picture)

        # Save the updated recipes to the JSON file
        with open('recipes.json', 'w') as file:
            json.dump(recipes, file, indent=4)
        st.experimental_rerun()
        st.success("Recipe added successfully!")

if __name__ == "__main__":
    main()