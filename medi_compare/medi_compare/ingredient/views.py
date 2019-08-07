from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient
from .models import Ingredient_name
from .models import Ingredient_unit
from .models import Ingredient_class
# Create your views here.

def index(request):
    return render(request, 'index.html')

class IngredientListView(ListView):
    model = Ingredient
    
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredientList'


class IngredientClassListView(ListView):
    model = Ingredient_class
    
    template_name = 'ingredient_class_list.html'
    context_object_name = 'ingredientClassList'

class IngredientNameListView(ListView):
    model = Ingredient_name
    
    template_name = 'ingredient_name_list.html'
    context_object_name = 'ingredientNameList'
    
class IngredientUnitListView(ListView):
    model = Ingredient_unit
    
    template_name = 'ingredient_unit_list.html'
    context_object_name = 'ingredientUnitList'
    
    