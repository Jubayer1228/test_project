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






Prove that your code is high quality (conforms to standards, is maintainable, is easy to enhance/modify:


1. By following the coding standards and conventions:
   Based on the programmimg language there are certain coding standards. For Python, we can follow PEP 8, for 
   Javascript we have ESLint and so on.
2. using Version Control:
   Utilizing version control systems like git to track changes, by collaborating with others and easily revert back 
   to previous versions if needed.
3. Modularizing Code:
   By Breaking our code into small, modular components such as functions, classes, modules which performs specific 
   tasks
4. Writing Clear Comments:
   By documenting the code using clear and concise comments, Explaining the purpose of the functions and classes
5. Avoiding code duplication:
   duplication of code blocks is a huge nightmare. By creating a functiona and calling those functions to avoid 
   repeatitive work
6. handle Errors Gracefully:
   By implementing proper Error handling to make sure the code is robust. Using try-catch blocks, exception handling 
   etc can be implemented to handle errors
7. Unit Testing:
   By writing unit testcases to verify the correctness of individual components.
8. Code Reviews:
   By Encouraging code reviews by peers or experienced developers.
9. maintaing a clean Git History:
    By commiting small, focused changes with meaningful commit messages.



What would you do ensure that expansion of the test app maintains good code quality?

This testapp named customers can be expanded.
1. each row has customers info. we can implement sort fucntion based on characters on the firstname or lastname fields.
2. customers list can be implemented as grid element and it can be multipage. In that case scolling to the next page or 
   limiting 10,15 or 20 customers per page would be useful. This is very useful features to have
3. adding customers link can be used differently. Instead of navigating to another html page, we can implement this as a pop 
   up window in that same page and once we have all the fields data provided to the text forms we can save them and it will 
   just close the pop up window.
4. We can also implement the underlying datanase with postgres which is a must for a production environment. sqllite is just 
   for example purpose or for small task.
5. In the main landing page, we can have a menu bar to begin with and then implement hover action whenever it requires.
6. all the javascript code can be in a seperate script and can be loaded in to the html page.
7. along with delete button, we can have save button similarly once we update them in that main page. No need to go to a 
   different page. though, its clear if we do so.
To ensure the testapp maintains good code quality, we can certainly follow the steps that we have discussed earlier.
we can adopt more strategy lik
   1. User Feedback: In a agile software development, It's very important step to accomodate user feedback
   2. Team Training: By keeping our Django team upto date to the latest enhancement and technologies. we can arrange 
      training and share each otehrs knowledge.
   3. Planning and Architecture: maintaining a clear Project roadmap and architectural guidlines along with long term vision.
   4. Regular Maintenance: regular maintenance is necessary and need to review the code in each Sprint and focusing on the 
      improving the quality of the code
   5. performance optimization: Django support different types of caching like per site cache, per view cache, template 
      cache, local file system based cache and redis cache. Based on the database transaction time, we can adopt required 
      caching mechanism to avoid performance bottleneck.
