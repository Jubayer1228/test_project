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
We need to add all the required fields before saving this new customer info. State field is a drop down menu where we can choose the state. Zip code is a 5 digit numeric field. I have added regex to make sure only 5 digit input value will be acceptable as a valid zipcode.

