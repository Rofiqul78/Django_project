from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import BlogTables

@login_required(login_url='/')
def dashboard(request):
    querydata =BlogTables.objects.all()
    context = {
   'table_data' : querydata
    }
    return render(request,'dashboard_index.html', context)



