from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.db import transaction

from dal import autocomplete

from .models import Effect

from .forms import EffectRegisterForm
# Create your views here.

class EffectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
            
        qs = Effect.objects.all()

        if self.q:
            qs = qs.filter(effect_name__istartswith=self.q)
        
        return qs

class EffectListView(ListView):
    model = Effect
    template_name = 'effect_list.html'
    context_object_name = 'effectList'
    
class EffectRegisterView(FormView):
    template_name = 'effect_register.html'
    form_class = EffectRegisterForm
    success_url = '/effect/register'
    
    def form_valid(self, form):
        with transaction.atomic():
            effect = Effect(
                effect_name = form.cleaned_data['effect'],
            )
            effect.save()
        return super().form_valid(form)
    