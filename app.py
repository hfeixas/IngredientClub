import falcon
import falcon_jsonify
from resources import *

app = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),
])

app.add_route('/recipes', Recipes())
app.add_route('/ingredients', Ingredients())
app.add_route('/api/list', GetRecipes())
