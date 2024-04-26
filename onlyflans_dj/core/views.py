from django.contrib.auth import login
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render, redirect
from product.models import Flan
import random
from .forms import SignUpForm, ContactFormForm

# Create your views here.
def frontpage(request):
    flanes = Flan.objects.all()
    random_flanes = random.sample(list(flanes), min(len(flanes), 8))
    context = {
        'flanes': random_flanes,
        'MEDIA_URL': settings.MEDIA_URL
               
               }

    return render(request, 'core/frontpage.html', context)


def signup(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request, user)

            return redirect('welcome/')
    else:
        form=SignUpForm()

    return render(request, 'core/signup.html', {'form':form})

def user_login(request):
    return render(request, 'core/login.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  
    else:
        form = ContactFormForm()

    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):

    return render(request, 'core/contact_success.html')

def welcome(request):
    flanes = Flan.objects.all()

    query = request.GET.get('query', '')
    if query:
        flanes= flanes.filter(Q(name__icontains=query) | Q(description__icontains=query))


    return render(request, 'core/welcome.html', {'flanes': flanes})


def about(request):

    return render(request, 'core/about.html')
