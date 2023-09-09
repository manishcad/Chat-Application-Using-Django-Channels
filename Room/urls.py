from django.urls import path
from . import views

urlpatterns=[
    path("",views.Rooms,name="Rooms"),
    path("<slug:slug>",views.room,name="Room"),
    
]