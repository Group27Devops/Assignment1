"""Module defined for using Flask framework"""
from flask import Flask, render_template, request
"""Module imported for using http requests"""
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Function defined for rendering index.html"""
    return render_template('index.html')

@app.route('/dishes')
def dishes():
    """Function defined for rendering dishes.html"""
    response = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood')
    data = response.json()
    return render_template('dishes.html', dishes=data['meals'])

@app.route('/recipe/<reciperecipeId>')
def recipe(recipeId):
    """Function defined for rendering recipe.html"""
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipeId}')
    data = response.json()
    recipe = data['meals'][0]
    ingredients = [recipe[f'strIngredient{i}'] for i in range(1, 21) if recipe[f'strIngredient{i}']]
    return render_template('recipe.html', recipe=recipe, ingredients=ingredients)

if __name__ == '__main__':
    """Here is the main app initialization"""
    app.run(debug=True)
