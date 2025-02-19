from django.shortcuts import render, redirect
from Base.models import Starter, Shawarma, ShawarmaPlate, LoadedShawarma, CombosForOne, CombosForTwo, HealthyShawarma, OnlyForCheeseLovers, AddOn
from Simplee.settings import logger

# Create your views here.
def index(request):
    logger.info("Home page rendered...")
    return render(request, "home.html")

def regulations_content(request):
    logger.info("Company Policies rendered...")
    return render(request, 'contents.html')

def about_us(request):
    logger.info("About Us Page rendered...")
    return render(request, 'about.html')

def menu_items(request):
    logger.info("Fetching all the menu items from databases...")
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
    logger.info("Menu Items rendered to the page...")
    logger.info("Menu page rendered...")

    return render(request, 'menu.html', context)

def contact_us(request):
    logger.info("Contact Us Page rendered...")
    return render(request, "contact.html")