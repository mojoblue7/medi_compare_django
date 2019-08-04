from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient
# Create your views here.

def index(request):
    return render(request, 'index.html')

class IngredientListView(ListView):
    model = Ingredient
    
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredientList'
    