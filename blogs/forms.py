from django import forms
from .models import BlogTables

class BlogTablesForm(forms.ModelForm):
    class Meta:
        model = BlogTables
        fields = '__all__'  # Use this to include all fields from the model
