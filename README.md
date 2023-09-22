# test_project
A webapp with Django

To run this project use the following command
# git clone https://github.com/Jubayer1228/test_project.git
Once we clone this repository, we can cd into the test_project root folder
from the root directory, we can issue the following command
# python manage.py runserver
If the command runs without any error, we will see this message "Starting development server at http://127.0.0.1:8000/". we can use the following link to access the webapp
http://127.0.0.1:8000/customers/

From the UI, now we can navigate to the Add Customer page by clicking the "Add Customer" link on the top right hand corner. This will open up a new page
"http://127.0.0.1:8000/customers/add/" where we can add necessary information to add any new customer.
We need to add all the required fields before saving this new customer info. State field is a drop down list where we can choose the state. Zip code is a 5 digit numeric field. I have added regex to make sure only 5 digit input value will be acceptable as a valid zipcode.

To update any customer info, we can click the link on the FirstName which will redirect us to a new page. This is quite similar to the Add Customer page. 

Steps to create a django webapp:

Creating a Django web app involves several steps. Here's a step-by-step guide to create a Django webapp.

Prerequisites:
1. Install Python, Django

Step1: Install Django
First, we need to install Django. we can do this using Python's package manager, pip:
pip install Django

Step2: Create a Django Project
django-admin startproject test_project

Step3: Create a Django App
Django projects are organized into apps. To create a new app use the following commands
cd test_project  # Navigate to your project directory
python manage.py startapp customers
we have created a webapp called customers 

Steps 4: Configure Settings
In our project's settings (projectname/settings.py), configure the database, static files, and other project-specific settings. Make sure to set DEBUG to False in production environments. For simplicity I have used the default sqlite db which has a customer table with six fields. To use postgres, we just simply edit the settings.py file in the DATABASES section. "ENGINE" params should be postgres and provide the Datbase NAME, USER, PASSWORD, HOST, PORT info as needed. We also need to register the app by adding "customers" in the INSTALLED_APPS section
