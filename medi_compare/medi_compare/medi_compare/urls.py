"""medi_compare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from ingredient.views import index, IngredientListView, IngredientNameListView, \
    IngredientUnitListView, IngredientClassListView, IngredientRegisterView, \
        IngredientNameAutocomplete, IngredientUnitAutocomplete, IngredientClassAutocomplete
from effect.views import EffectListView, EffectRegisterView, EffectAutocomplete

urlpatterns = [
    url(r'^ingredient-class-autocomplete/$', IngredientClassAutocomplete.as_view(create_field='ingredient_class'), name='ingredient-class-autocomplete-create',),
    url(r'^ingredient-class-autocomplete/$', IngredientClassAutocomplete.as_view(), name='ingredient-class-autocomplete',),

    url(r'^ingredient-name-autocomplete/$', IngredientNameAutocomplete.as_view(create_field='ingredient_name'), name='ingredient-name-autocomplete-create',),
    url(r'^ingredient-name-autocomplete/$', IngredientNameAutocomplete.as_view(), name='ingredient-name-autocomplete',),

    url(r'^ingredient-unit-autocomplete/$', IngredientUnitAutocomplete.as_view(create_field='ingredient_unit'), name='ingredient-unit-autocomplete-create',),
    url(r'^ingredient-unit-autocomplete/$', IngredientUnitAutocomplete.as_view(), name='ingredient-unit-autocomplete',),

    url(r'^effect-name-autocomplete/$', EffectAutocomplete.as_view(create_field='effect_name'), name='effect-name-autocomplete-create',),
    url(r'^effect-name-autocomplete/$', EffectAutocomplete.as_view(), name='effect-name-autocomplete',),

    path('admin/', admin.site.urls),
    path('', index),
    path('ingredient/list/', IngredientListView.as_view()),
    path('ingredient/register/', IngredientRegisterView.as_view()),
    path('ingredient_name/list/', IngredientNameListView.as_view()),
    path('ingredient_unit/list/', IngredientUnitListView.as_view()),
    path('ingredient_class/list/', IngredientClassListView.as_view()),
    path('effect/list/', EffectListView.as_view()),
    path('effect/register/', EffectRegisterView.as_view()),
]
