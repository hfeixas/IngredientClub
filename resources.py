from __future__ import unicode_literals
import falcon_jsonify
# import youtube_dl
from settings import db
from models.ingredient_model import Recipe
import os
import falcon
import json
import jinja2
from jinja2 import Environment, FileSystemLoader



def load_template(name):
    path = os.path.join('templates', name)
    with open(os.path.abspath(path), 'r') as fp:
        template_str = fp.read()
    template = Environment(loader=FileSystemLoader("templates/")).from_string(template_str)

    return template

class HomePage(object):
    def on_get(self, req, resp):
        # Load Recipes On home
        rows = []
        for i in Recipe.objects:
            row = {
                'name': i.name,
                'id': i.id
            }
            rows.append(row)
        # End On Loading Recipes

        template = load_template('home.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(rows=rows)

class GetRecipes(object):
    def on_get(self, req, resp):
        rows = []
        for i in Recipe.objects():
            row = {
                'name': i.name,
            }
            rows.append(row)
        resp.status = falcon.HTTP_200
        resp.json = rows

class AddRecipe(object):
    def on_post(self, req, resp):
        data = req.params
        name = data['name']
        description = data['description']
        row = Recipe(
            name = name,
            description=description
        )
        row.save()
        resp.status = falcon.HTTP_201
        resp.json = json.dumps({'id': str(row.id)})

class EditRecipe(object):
    def on_put(self, req, resp):
        data = req.params
        name = data['name']
        id = data['id']
        row = Recipe(id = id)
        row.update(name=name)
        resp.status = falcon.HTTP_200
        resp.json = json.dumps({'id': str(row.id)})

class DelRecipe(object):
    def on_delete(self, req, resp):
        data = req.params
        id = data['id']
        recipe = Recipe.objects(id=id)
        recipe.delete()
        resp.json = {'id': str(id)}
        resp.status = falcon.HTTP_204
