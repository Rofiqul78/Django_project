from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import login as auth_login



def signup_page(request):
    if request.method == "GET":
        return render(request,'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # password2 = request.POST.get('password2')
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect ('login_page')
    return render(request,'signup.html')

def login_page(request):
    if request.method == "GET" :
        return render(request, 'login.html' )
    
    elif request.method == "POST" :
        input_username = request.POST ['username']
        input_password = request.POST ['password']
        user= auth.authenticate(username=input_username, password=input_password)
        print(user)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard_urls')
        else:
            messages.error (request,"Login credentials are not matching")
            return render(request, 'login.html')

def logout_session(request): 
    auth.logout(request)      
    return redirect('login_page') 

