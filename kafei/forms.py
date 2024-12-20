from django import forms
from .models import Info,Bookingform
from django .forms import TextInput,Textarea
class Detailsform(forms.ModelForm):
    class Meta:
        model=Info
        fields=['name','email','message']
        widgets={
            'name':TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control", 
                    "placeholder":"write your Full Name"
                }
            ),
            'email':TextInput(
                attrs={
                    "type":"email",
                    "class":"form-control", 
                    "placeholder":"Email id"
                }
            ),
            'message':Textarea(
                attrs={
                    "class":"form-control", 
                    "placeholder":"Write something ....",
                    "style":"height:150px;"
                }
            )
        }
class Bookingform(forms.ModelForm):
    class Meta:
        model=Bookingform
        fields=['name','phone','date','time','no_of_person','msg']
        widgets={
            'name':TextInput(
                attrs={
                  "type":"text",
                "placeholder":"Full Name", 
                  "style":"width: 300px; height: 25px; background-color: rgb(241, 245, 245); margin-left: 15px; margin-top: 15px;"  
                }
            ),
            'phone':TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"Phone Number",
                    "style":"width: 300px; height: 25px;  background-color: rgb(241, 245, 245);  margin-left: 15px; margin-top: 10px;"
                }
            ),
            'date':TextInput(
                attrs={
                    "type":"date", 
                    "style":"width: 140px; height: 25px; background-color: rgb(241, 245, 245);  margin-left: 15px; margin-top: 15px;"
                }
            ),
            'time':TextInput(
                attrs={
                    "type":"time", 
                    "style":"width: 140px; height: 25px; margin-left: 20px; background-color: rgb(241, 245, 245);  margin-left: 17px; margin-top: 15px;" 
                }
            ),
            'no_of_person':TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"No of Persons", 
                    "style":"width: 300px; height: 25px; background-color: rgb(241, 245, 245);  margin-left: 15px; margin-top: 15px;"
                }
            ),
            'msg':TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"Message", 
                    "style":"width: 300px; height: 100px; background-color: rgb(241, 245, 245);  margin-left:15px; margin-top: 20px; padding-bottom: 10px;"
                }
            )
        }        