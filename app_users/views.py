from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_profile
from django.contrib.auth.models import User
from django.contrib import auth
from university.models import Institute
# Create your views here.
def index(request):
    institute=Institute.objects.all()
    context={
        'institute':institute
    }
    return  render(request,'home.html',context)

def register(request):
    registered=False
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        bio=request.POST['bio'] 
        try:
            user=User.objects.get(username=username)
            return render(request,'app_users/registration.html',{'error':'Username already taken!'}) 
        except User.DoesNotExist:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            newuser=user_profile()
            if bio:
                newuser.bio=bio
            newuser.user=user
            newuser.save() 
            auth.login(request,user)
            registered=True
            return redirect('index')
    elif request.method=='GET':
        return render(request,'app_users/registration.html')            
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is None:
            return  render(request,'app_users/login.html',{'error':'Incorrect username or password'})

        else:
            auth.login(request,user)
            return redirect('index')
                 
    elif request.method =='GET':
        return  render(request,'app_users/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'home.html')

