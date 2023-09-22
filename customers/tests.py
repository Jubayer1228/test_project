from django.test import TestCase
#from django.test import SimpleTestCase
from django.urls import reverse
from .models import Customer

# Create your tests here.
# testing customers main page 
class CustomersTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)

    def test_url_availability_by_name(self):
        response= self.client.get(reverse("customers"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):  
        response = self.client.get(reverse("customers"))
        self.assertTemplateUsed(response, "index.html")

    def test_template_content(self):
        response = self.client.get(reverse("customers"))
        self.assertContains(response, "<h1>Customers</h1>")
        self.assertNotContains(response, "Not on the page")


# testing add_customer_info page
class CustomersAddTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/customers/add/")
        self.assertEqual(response.status_code, 200)

    def test_url_availability_by_name(self):
        response= self.client.get(reverse("add"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("add"))
        self.assertTemplateUsed(response, "add.html")

    def test_template_content(self):
        response = self.client.get(reverse("add"))
        self.assertContains(response, "<h1>Add Customer</h1>")
        self.assertNotContains(response, "Not on the page")

