import json
from mongoengine import *
import datetime

class CategoryModel(Document):
   id = SequenceField(primary_key=True)
   name = StringField(max_length=200, required=True)
   type = StringField(max_length=200, required=True)
   
   def __str__(self) -> str:
      return self.name

class IngredientModel(Document):
   id = SequenceField(primary_key=True)
   name = StringField(max_length=200, required=True)
   description = StringField(max_length=200, required=True)
   category = ReferenceField(CategoryModel, required=True)
   
   def get_cat(self):
      category = CategoryModel.objects.filter(id=self.category)
      category_data = json.loads(category.to_json())
      category_name = category_data['name']
      
      return category_name

   def __str__(self) -> str:
      return self.name

class RecipeIngredientModel(Document):
   id = SequenceField(primary_key=True)
   ingredient = ReferenceField(IngredientModel)
   unit_of_measure = StringField(max_length=200, required=True)
   quantity = StringField(max_length=200, required=True)

class RecipeModel(Document):
   id = SequenceField(primary_key=True)
   name = StringField(max_length=200, required=True)
   category = ReferenceField(CategoryModel)
   description = StringField(max_length=200)
   ingredients= ListField(ReferenceField(RecipeIngredientModel))
   prep_time = StringField(max_length=200)
   cook_time = StringField(max_length=200)
   steps = ListField()