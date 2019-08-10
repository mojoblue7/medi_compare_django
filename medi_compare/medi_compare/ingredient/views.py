from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.db import transaction

from dal import autocomplete

from .models import Ingredient, Ingredient_name, Ingredient_unit, Ingredient_class

from .forms import IngredientRegisterForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

class IngredientNameAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
            
        qs = Ingredient_name.objects.all()

        if self.q:
            qs = qs.filter(ingredient_name__istartswith=self.q)
        
        return qs

class IngredientUnitAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
             
        qs = Ingredient_unit.objects.all()
        if self.q:
            qs = qs.filter(ingredient_unit__istartswith=self.q)
          
        return qs

class IngredientClassAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
             
        qs = Ingredient_class.objects.all()
        if self.q:
            qs = qs.filter(ingredient_class__istartswith=self.q)
          
        return qs

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
    
class IngredientRegisterView(FormView):
    template_name = 'ingredient_register.html'
    form_class = IngredientRegisterForm
    success_url = '/ingredient/register'
    
    def form_valid(self, form):
        with transaction.atomic():
            ingredient = Ingredient(
                ingredient_name = form.cleaned_data['ingredient_name'],
                ingredient_class = form.cleaned_data['ingredient_class'],
                ingredient_volume = form.cleaned_data['ingredient_volume'],
                ingredient_unit = form.cleaned_data['ingredient_unit'],
                ingredient_detail_content = form.cleaned_data['ingredient_detail_content']
            )
            ingredient.save()
        return super().form_valid(form)
    