from django.db import models

# Create your models here.
# This will create a table in the database, This Customer table has six attribute. Django supports serialization which actually converts python
# object to json or xml and vice versa. Django rest framework has more flexible serialization to handle more complex objects.
class Customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname  = models.CharField(max_length=255)
  address   = models.CharField(max_length=255)
  city      = models.CharField(max_length=255)
  zipcode   = models.IntegerField()
  state     = models.CharField(max_length=255)


  def __str__(self):
      return f"Info: {self.firstname} {self.lastname} {self.address} {self.city} {self.zipcode} {self.state}"
