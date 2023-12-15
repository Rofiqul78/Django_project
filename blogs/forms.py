from django import forms
from .models import BlogTables

class BlogTablesForm(forms.ModelForm):
    class Meta:
        model = BlogTables
        fields = ['student_name', 'order_number', 'imageField']  

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    