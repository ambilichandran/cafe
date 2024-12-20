from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Menu,Bookingform
from .forms import Detailsform, Bookingform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
def index(request):
    return render (request,"index.html")
def about(request):
    return render (request,"about.html")
def menu(request):
    item=Menu.objects.all()
    return render (request,"menu.html",{"item":item})
def contact(request):
    form=Detailsform()
    if request.method=='POST':
        form=Detailsform(request.POST)
        if form.is_valid():
            form.save()
            form=Detailsform()
            return redirect("contact")
    return render (request,"contact.html",{"form":form})
def reserve_a_table(request):
    reserve_a_table(request)
    return redirect("book")
@login_required
def book(request):
    form=Bookingform()
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            form=Bookingform()
            return redirect("book")
    return render (request,"book.html",{"form":form})
def registration(request):
    form=UserCreationForm() 
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=UserCreationForm() 
            return redirect("login")
        return redirect("login") 
    return render(request,"registration.html",{"form":form})
def logout(request):
    return redirect("/")