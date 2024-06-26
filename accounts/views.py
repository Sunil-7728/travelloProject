from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']

       user = auth.authenticate(username = username, password = password)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request,'Invalid credentials')
           return redirect('/')

    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       password=request.POST['password']
       email = request.POST['email']
       confirm_password=request.POST['confirm_password']
       if password==confirm_password:
           if User.objects.filter(username=username).exists():
               messages.info(request,'Username taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request, 'email taken')
               return redirect('register')
           else:
               user = User.objects.create_user(username=username, password=password, email=email,first_name = first_name,last_name=last_name)
               user.save()
               print('user created')
               return redirect('login')
       else:
           messages.info(request,'password not matching')
           return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')