from django.urls import path
from . import views

urlpatterns=[
    path("",views.Home,name="Home"),
    path("Signup",views.Signup,name="Signup"),
    path("Logout_page",views.Logout_Page,name="Logout_Page"),
    path("Login_page",views.Login_Page,name="Login_Page"),
]