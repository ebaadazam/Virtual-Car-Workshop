from django.contrib import admin
from django.urls import path

# Imported manually
from Myapp import views

# manually
urlpatterns = [
    path("", views.index, name='Myapp'),
    
    path("about", views.about, name='about'),
    
    path("services", views.services, name='services'),
    
    path("contact", views.contact, name='contact'),
    
    path("drop1", views.drop1, name='drop1'), 
    
    path("drop2", views.drop2, name='drop2'), 
     
    path("drop3", views.drop3, name='drop3'), 
      
    path("drop4", views.drop4, name='drop4')
]
