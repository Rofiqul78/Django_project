from django.shortcuts import render, redirect
from .models import BlogTables
from django.http import HttpResponse

def save_blogs(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        order_number = request.POST['order_number']
        try:
            BlogTables.objects.create(student_name=student_name, order_number=order_number)
            return HttpResponse("Your information has been successfully recorded")
        except Exception as e:
            print(str(e))
            return HttpResponse("An error occurred while saving the information")
    else:
        # Handle GET request or other HTTP methods if needed
        return HttpResponse("Invalid request method")


