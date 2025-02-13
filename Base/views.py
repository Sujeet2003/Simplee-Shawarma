from django.shortcuts import render
from Base.models import Starter


# Create your views here.
def index(request):
    return render(request, "home.html")

def regulations_content(request):
    return render(request, 'contents.html')

def about_us(request):
    return render(request, 'about.html')

def menu_items(request):
    starter_items = Starter.objects.all()
    context = {
        'starter_items': starter_items,
    }
    return render(request, 'menu.html', context)