from django.shortcuts import render, redirect
from Base.models import Starter, Shawarma, ShawarmaPlate, LoadedShawarma, CombosForOne, CombosForTwo, HealthyShawarma, OnlyForCheeseLovers, AddOn

# Create your views here.
def index(request):
    return render(request, "home.html")

def regulations_content(request):
    return render(request, 'contents.html')

def about_us(request):
    return render(request, 'about.html')

def menu_items(request):
    # Fetch all items for each category
    starter_items = Starter.objects.all()
    shawarma_items = Shawarma.objects.all()
    shawarma_plate_items = ShawarmaPlate.objects.all()
    loaded_shawarma_items = LoadedShawarma.objects.all()
    combos_for_one_items = CombosForOne.objects.all()
    combos_for_two_items = CombosForTwo.objects.all()
    healthy_shawarma_items = HealthyShawarma.objects.all()
    cheese_lovers_items = OnlyForCheeseLovers.objects.all()
    add_on_items = AddOn.objects.all()

    # Pass the items to the template
    context = {
        'starter_items': starter_items,
        'shawarma_items': shawarma_items,
        'shawarma_plate_items': shawarma_plate_items,
        'loaded_shawarma_items': loaded_shawarma_items,
        'combos_for_one_items': combos_for_one_items,
        'combos_for_two_items': combos_for_two_items,
        'healthy_shawarma_items': healthy_shawarma_items,
        'cheese_lovers_items': cheese_lovers_items,
        'add_on_items': add_on_items,
    }

    return render(request, 'menu.html', context)

def contact_us(request):
    return render(request, "contact.html")