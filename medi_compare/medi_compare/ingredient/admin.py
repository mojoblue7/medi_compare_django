from django.contrib import admin
from .models import Ingredient, IngredientName

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientName)