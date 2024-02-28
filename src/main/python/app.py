"""Modules defined for using requests lib and Flask framework"""
import requests
from flask import Flask, render_template


app = Flask(__name__)
BASE_URL = "https://www.themealdb.com/api/json/v1"

@app.route('/')
def index():
    """Function defined for rendering index.html"""
    return render_template('index.html')

@app.route('/dishes')
def dishes():
    """Function defined for rendering dishes.html"""
    response = requests.get(f'{BASE_URL}/1/filter.php?c=Seafood', timeout=50)
    data = response.json()
    return render_template('dishes.html', dishes=data['meals'])

@app.route('/recipe/<recipe_id>')
def recipe_dish(recipe_id):
    """Function defined for rendering recipe.html"""
    response = requests.get(f'{BASE_URL}/1/lookup.php?i={recipe_id}', timeout=50)
    data = response.json()
    recipe = data['meals'][0]
    ingredients = [recipe[f'strIngredient{i}'] for i in range(1, 21) if recipe[f'strIngredient{i}']]
    return render_template('recipe.html', recipe=recipe, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)
