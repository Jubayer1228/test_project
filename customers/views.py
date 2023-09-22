from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Customer
# Create your views here.

def customers(request):
    mycustomers= Customer.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mycustomers': mycustomers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

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

def delete(request, id):
  customer= Customer.objects.get(id=id)
  customer.delete()
  return HttpResponseRedirect(reverse('customers'))


def update(request, id):
  mycustomers= Customer.objects.get(id=id)
  template= loader.get_template('update.html')
  context = {
    'mycustomers': mycustomers,
  }
  return HttpResponse(template.render(context, request))

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
