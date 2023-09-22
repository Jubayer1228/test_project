from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add, name= 'add'),
    path('customers/add/addrecord/', views.addrecord, name='addrecord'),
    path('customers/delete/<int:id>',views.delete, name='delete'),
    path('customers/update/<int:id>',views.update, name='update'),
    path('customers/update/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
]
