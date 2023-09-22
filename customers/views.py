# import all the necessary packages here, 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Customer
# Create your views here.
# we have created a folder called template inside the test_project directory. This folder will have all the htmls needed for the webapp
# to process the request for the first page "customers", we have created a function that will handle the requets and serve the HttpResponse 
# 
def customers(request):
    mycustomers= Customer.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mycustomers': mycustomers,
    }
    return HttpResponse(template.render(context, request))

# add function will process the request and will send the HttpResponse. template variable calls the loader.get_template and takes a html page as an argument and 
# finally render that views
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
# addrecord function process the post request and converts the data to python object and save them into the database
def addrecord(request):
  a= request.POST['first']
  b= request.POST['last']
  c= request.POST['address']
  d= request.POST['city']
  e= request.POST['zipcode']
  f= request.POST['state']
  
  customer= Customer(firstname=a, lastname=b, address=c, city=d, zipcode=e, state=f)
  customer.save()
  return HttpResponseRedirect(reverse('customers'))

# given the id of the customer, we can get call the customer model objects and delete that particular customer
def delete(request, id):
  customer= Customer.objects.get(id=id)
  customer.delete()
  return HttpResponseRedirect(reverse('customers'))
# based on the customer id, update function get the model from the database using the id

def update(request, id):
  mycustomers= Customer.objects.get(id=id)
  template= loader.get_template('update.html')
  context = {
    'mycustomers': mycustomers,
  }
  return HttpResponse(template.render(context, request))

# update record function get the customer model from the post request and them replace them by reassigning cutomer model objects and save them in the database
def updaterecord(request, id):
  a= request.POST['first']
  b= request.POST['last']
  c= request.POST['address']
  d= request.POST['city']
  e= request.POST['zipcode']
  f= request.POST['state']

  customer=Customer.objects.get(id=id)
  customer.firstname=a
  customer.lastname=b
  customer.address=c
  customer.city=d
  customer.zipcode=e
  customer.state=f
  customer.save()
  return HttpResponseRedirect(reverse('customers'))
