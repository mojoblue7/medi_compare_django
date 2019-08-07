from django.contrib import admin
from .models import Ingredient, Ingredient_name, Ingredient_unit, Ingredient_class
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Ingredient_name)
admin.site.register(Ingredient_unit)
admin.site.register(Ingredient_class)