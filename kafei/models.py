from django.db import models
from django.contrib.auth.models import User
class Menu(models.Model):
    item=models.CharField(max_length=50,blank=None)
    price=models.CharField(max_length=50,blank=None)
    image=models.ImageField(max_length=500,blank=None,upload_to="image")
    def __str__(self):
        return self.item
class Info(models.Model):
    name=models.CharField(max_length=50,blank=None)
    email=models.EmailField()
    message=models.TextField(max_length=150,blank=None)
    def __str__(self):
        return self.name
class Bookingform(models.Model):
    name=models.CharField(max_length=50,blank=None)
    phone=models.CharField(max_length=100,blank=None)
    date=models.DateField()
    time=models.TimeField()
    no_of_person=models.CharField(max_length=20,blank=None)
    msg=models.TextField(max_length=150,blank=True)
    def __str__(self):
        return self.name
