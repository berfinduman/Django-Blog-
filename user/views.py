from django.shortcuts import render,HttpResponse, redirect
from .froms import Register, Login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def register(request):    
    form=Register(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser= User(username= username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Hoşgeldin {}".format(username))
        return redirect("index")
    

        
    context={"form": form}
    return render(request, "register.html",context)
    
  
    
def loginUser(request):
    form=Login(request.POST or None)
    context={"form": form}
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(username=username, password= password)
        
        if user is None:
            messages.info(request, "Hatalı Giriş")
            return render(request,"login.html",context)

        login(request,user)
        messages.success(request, "Hoşgeldin {}".format(username))
        
        return redirect("index")
    return render(request, "login.html",context)
    
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız.")
    return redirect("index")