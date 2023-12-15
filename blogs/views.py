from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogTables
from .forms import BlogTablesForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


@login_required
def save_blogs(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        order_number = request.POST['order_number']
        image_data = request.FILES['image_upload']
        try:
            db_data = BlogTables.objects.create(student_name=student_name, order_number=order_number, imageField=image_data)
            form = BlogTablesForm(request.POST, instance=db_data)
            if form.is_valid():
                form.save()
        except:
            return HttpResponse("Error: Data not saved.")
    return render(request, 'dashboard.urls')


@login_required
def delete_blogs(request, pk): 
    try:
        BlogTables.objects.filter(id=pk).delete()
        messages.success(request, "Data successfully deleted.")
    except Exception as e:
        print(str(e))
        messages.success(request, "Data successfully deleted.")

@login_required       
def update_html(request, pk):
    try:
        db_data = BlogTables.objects.get(id=pk)
    except BlogTables.DoesNotExist:
        messages.error(request, "Record not found.")
        return redirect('dashboard_urls')
    
    if request.method == "POST":
        form = BlogTablesForm(request.POST, request.FILES, instance=db_data)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Data successfully updated.")
            except ValidationError as e:
                messages.error(request, f"Validation error: {e}")
            except Exception as e:
                messages.error(request, f"Error updating data: {e}")
            return redirect('dashboard_urls')
        else:
            messages.error(request, "Form validation error.")
    else:
        form = BlogTablesForm(instance=db_data)
    return render(request, 'update_data.html', {'form': form, 'data': db_data})
