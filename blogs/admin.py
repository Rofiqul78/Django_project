from django.contrib import admin
from .models import BlogTables

# Register your models here.

class ShowFields(admin.ModelAdmin):
    fields = ('id','student_name', 'order_number','imageField''created_at')
    list_display = ('id', 'student_name', 'order_number','imageField')
    list_filter = ('order_number',)
    search_fields = ('order_number',)
    
    
admin.site.register(BlogTables, ShowFields)   