from __future__ import unicode_literals
import falcon_jsonify
from settings import db
from models.ingredient_model import RecipeModel, IngredientModel, CategoryModel, RecipeIngredientModel
from jinja2 import Environment, FileSystemLoader
import jinja2
import os
import falcon
import json



def load_template(name):
    path = os.path.join('templates', name)
    with open(os.path.abspath(path), 'r') as fp:
        template_str = fp.read()
    template = Environment(loader=FileSystemLoader("templates/")).from_string(template_str)

    return template

class Recipes(object):
    def on_get(self, req, resp):
        recipes = RecipeModel.objects.all()
        data = json.loads(recipes.to_json())


        template = load_template('recipes.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(rows=data)

    def on_post(self, req, resp):
        data = req.params
        name = data['name']
        description = data['description']
        row = RecipeModel(
            name = name,
            description=description
        )
        row.save()
        resp.status = falcon.HTTP_201
        resp.json = json.dumps({'id': str(row.id)})
    
    def on_put(self, req, resp):
        data = req.params
        name = data['name']
        id = data['id']
        row = RecipeModel(id = id)
        row.update(name=name)
        resp.status = falcon.HTTP_200
        resp.json = json.dumps({'id': str(row.id)})

    def on_delete(self, req, resp):
        data = req.params
        id = data['id']
        recipe = RecipeModel.objects(id=id)
        recipe.delete()
        resp.json = {'id': str(id)}
        resp.status = falcon.HTTP_204

class Ingredients(object):
    def on_get(self, req, resp):
        ingredients = IngredientModel.objects.all()
        categories = CategoryModel.objects.all()
        ingredient_data = json.loads(ingredients.to_json())
        category_data = json.loads(categories.to_json())
        for i in ingredient_data:
            category_id = i['category']
            for item in category_data:
                print(item)
                if item['_id'] == category_id:                    
                    i['category_name'] = item['name']
                    i['type'] = item['type']

        template = load_template('ingredients.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(
            ingredients=ingredient_data,
            categories= category_data
            )

    def on_post(self, req, resp):
        data = req.params
        name = data['name']
        description = data['description']
        category = int(data['category'])
        row = IngredientModel(
            name = name,
            description=description,
            category = category
        )
        row.save()
        resp.status = falcon.HTTP_201
        resp.json = json.dumps({'id': str(row.id)})
    
    def on_delete(self, req, resp):
        data = req.params
        id = data['id']
        print(id)
        ingredient = IngredientModel.objects(id=id)
        ingredient.delete()
        resp.json = {'id': str(id)}
        resp.status = falcon.HTTP_204

class GetRecipes(object):
    def on_get(self, req, resp):
        rows = []
        for i in RecipeModel.objects():
            row = {
                'name': i.name,
                'description': i.description
            }
            rows.append(row)
        resp.status = falcon.HTTP_200
        resp.json = rows
