from django .urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("menu",views.menu,name="menu"),
    path("contact",views.contact,name="contact"),
    path("reserve_a_table",views.reserve_a_table,name="reserve_a_table"),
    path("book",views.book,name="book"),
    path("registration",views.registration,name="registration"),
    path("logout",views.logout,name="logout"),
]