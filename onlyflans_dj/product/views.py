from django.shortcuts import render, get_object_or_404
from .models import Flan

def flan(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    return render(request, 'product/flan.html', {'flan' : flan})