# import necessary packages as needed.
# we also need to import the views.py as to include urlspattern, we need to call the functions on the views.py
from django.urls import path
from . import views

# add all the urls here, path function takes three arguments. first, we need to add the urls, then we need to call the function and finally we can give a name of the ursl.
# we can add optional arguments too.
urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add, name= 'add'),
    path('customers/add/addrecord/', views.addrecord, name='addrecord'),
    path('customers/delete/<int:id>',views.delete, name='delete'),
    path('customers/update/<int:id>',views.update, name='update'),
    path('customers/update/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
]
