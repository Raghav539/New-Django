from django.shortcuts import render, get_object_or_404 , redirect
from .models import Main


# Create your views here.

def home(request):

    return render(request,'front/home.html')

def about(request):

    return render(request,'front/about.html')
def contact(request):

    return render(request,'front/contact.html')