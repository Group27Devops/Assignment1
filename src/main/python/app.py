from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dishes')
def dishes():
    response = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood')
    data = response.json()
    return render_template('dishes.html', dishes=data['meals'])

@app.route('/recipe/<id>')
def recipe(id):
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
    data = response.json()
    recipe = data['meals'][0]
    ingredients = [recipe[f'strIngredient{i}'] for i in range(1, 21) if recipe[f'strIngredient{i}']]
    return render_template('recipe.html', recipe=recipe, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)
