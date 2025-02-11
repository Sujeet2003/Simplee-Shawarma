from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "home.html")

def regulations_content(request):
    return render(request, 'contents.html')

def about_us(request):
    return render(request, 'about.html')