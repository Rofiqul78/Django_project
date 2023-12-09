# from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello world!")

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
            return redirect('dashboard_url')
        else:
            messages.error(request, "the username or password or both are not matching")
            return render(request, 'login.html' )
