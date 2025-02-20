from django.test import TestCase
from django.urls import reverse, resolve
from Base.models import *

class ModelTests(TestCase):
    def setUp(self):
        self.starter = Starter.objects.create(
            items_name="Garlic Bread Shawarma",
            sub_items_name="Cheese Garlic Bread",
            half_price=99.0,
            full_price=149.0
        )
    
    def test_model_creation(self):
        self.assertEqual(self.starter.items_name, "Garlic Bread Shawarma")
        self.assertEqual(self.starter.sub_items_name, "Cheese Garlic Bread")
        self.assertEqual(self.starter.half_price, 99.0)
        self.assertEqual(self.starter.full_price, 149.0)

class ViewTests(TestCase):
    def test_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
    
    def test_about(self):
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
    
    def test_menu(self):
        response = self.client.get(reverse("menu_items"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")
    
    def test_contact(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

class URLTests(TestCase):
    def test_urls(self):
        urls = [
            ("home", "/"),
            ("about_us", "/about-simplee-shawarma/"),
            ("menu_items", "/menu-of-simplee-shawarma/"),
            ("contact_us", "/contact-us/"),
        ]
        
        for name, path in urls:
            self.assertEqual(reverse(name), path)
            self.assertEqual(resolve(path).view_name, name)

if __name__ == "__main__":
    TestCase.main()
