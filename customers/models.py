from django.db import models

# Create your models here.
class Customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname  = models.CharField(max_length=255)
  address   = models.CharField(max_length=255)
  city      = models.CharField(max_length=255)
  zipcode   = models.IntegerField()
  state     = models.CharField(max_length=255)
