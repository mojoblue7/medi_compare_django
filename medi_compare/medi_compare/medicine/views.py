from django.shortcuts import render

from .models import Medicine

# Create your views here.

class MedicineNameListView(ListView):
    model = Medicine
    template_name = 'medicine_list.html'
    context_object_name = 'medicineList'