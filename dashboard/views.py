from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import BlogTables

@login_required(login_url='/')
def dashboard(request):
    query = request.GET.get('query')
    if query:
        query_data = BlogTables.objects.filter(order_number__icontains=query)
    else:
        query_data = BlogTables.objects.all()

    context = {'table_data': query_data}
    return render(request, 'dashboard_index.html', context)
