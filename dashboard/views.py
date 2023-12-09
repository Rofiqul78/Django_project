from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def dashboard(request):
    return render(request,'dashboard_index.html')



# from django.shortcuts import render
# from django.http import HttpResponse

# def dashboard(request):
#     # Your view logic for the dashboard home page
#     return render(request, 'dashboard_index.html')

# def dashboard_profile(request, username):
#     # Your view logic for the user profile in the dashboard
#     return render(request, 'dashboard/profile.html', {'username': username})
