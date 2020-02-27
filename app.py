import falcon
import falcon_jsonify
from resources import HomePage, GetRecipes, DelRecipe, AddRecipe, EditRecipe
app = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),
])
app.add_route('/', HomePage())
app.add_route('/api/list', GetRecipes())
app.add_route('/api/add', AddRecipe())
app.add_route('/api/del', DelRecipe())
app.add_route('/api/edit', EditRecipe())
