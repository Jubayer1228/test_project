from django.test import TestCase
#from django.test import SimpleTestCase
from django.urls import reverse
from .models import Customer

# Create your tests here.
# testing customers main page 
class CustomersTests(TestCase):


    #   test_url_exists_at_correct_location method makes a HTTP request to the provided path and checks if the result code is successful.
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)

    #   test_url_availability_by_name methods construct a URL from the given name and make a HTTP request 
    #   to the created URL, then checks the status code of the request.
    def test_url_availability_by_name(self):
        response= self.client.get(reverse("customers"))
        self.assertEqual(response.status_code, 200)
    
    #   test_template_name_correct method checks if the correct template is loaded when the specified path is visited.
    def test_template_name_correct(self):  
        response = self.client.get(reverse("customers"))
        self.assertTemplateUsed(response, "index.html")
        
    # setUpTestData(cls) method is marked @classmethod since its executed first when the class is executed.
    # Within this function, we create Customer objects stored in a temporary test database and used throughout the test class.   
    @classmethod
    def setUpTestData(cls):
        number_of_customers = 10
        for customer_id in range(number_of_customers):
            Customer.objects.create(firstname=f"John{customer_id}", lastname=f"Doe{customer_id}", address=f"sherman{customer_id}", city="Denver", zipcode=80011, state="CO")
    
    #   test_template_content method checks if the correct header is available or not generally any content can be checked.
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

