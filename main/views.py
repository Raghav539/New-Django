from django.shortcuts import render, get_object_or_404 , redirect
from .models import Main


# Create your views here.

def home(request):

    sitename="MySite|Home"

    return render(request,'front/home.html', {'sitename':sitename})

def about(request):
    sitename="MySite|About"

    return render(request,'front/about.html', {'sitename':sitename})
def contact(request):
    sitename="MySite|Contact"

    return render(request,'front/contact.html', {'sitename':sitename})