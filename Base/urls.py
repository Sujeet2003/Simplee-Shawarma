from django.urls import path
from Base import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contents_about_rules_and_regulations/', views.regulations_content, name="rules_and_regulations"),
    path('about-simplee-shawarma/', views.about_us, name='about_us'),
    path('menu-of-simplee-shawarma/', views.menu_items, name="menu_items"),
    path('contact-us/', views.contact_us, name="contact_us"),
]