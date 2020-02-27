from mongoengine import *
import datetime

class Ingredient(Document):
   name = StringField(max_length=200, required=True)
   def __unicode__(self):
      return self.name
      
class Recipe(Document):
   name = StringField(max_length=200, required=True)
   description = StringField(max_length=200)
   ingredients= ListField(ReferenceField(Ingredient))
   
