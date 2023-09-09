from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    return render(request,'frontpage.html')


def Signup(request):
    if request.method == "POST":
       
        form=SignupForm(request.POST)
     
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("Home")
        
    else:
        form=SignupForm()
    context={'form':form}

    return render(request,'signup.html',context)

def Logout_Page(request):
    logout(request)
    return redirect("Login_Page")

def Login_Page(request):
    error=""
    if request.method=="POST":
        print("This is a Post Request")
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("Home")
        else:
            error="User Not Found"
    context={"error":error}
    print(error)
    return render(request,'login.html',context)