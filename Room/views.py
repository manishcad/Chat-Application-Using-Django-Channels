from django.shortcuts import render,redirect
from .models import Room
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
# Create your views here.

@login_required(login_url="Login_Page")
def Rooms(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'rooms.html',context)

@login_required(login_url="Login_Page")
def room(request,slug):

    try:
        room=Room.objects.get(slug=slug)
        msg=Message.objects.filter(room=room)
    except Exception as e:
        print(e)
     
        messages.warning(request,"Room Does Not Exists")
        return redirect("Rooms")
    
    context={'room':room,'messages':msg}
    return render(request,'room.html',context)