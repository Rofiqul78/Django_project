from django.db import models


# Create your models here.

class BlogTables(models.Model):
    student_name = models.CharField(max_length=100, null=False, blank=False)
    # Add the new non-nullable field with a default value
    order_number = models.IntegerField(default=0)  # Replace 0 with your desired default value
    # photo = models.ImageField(upload_to='blog_images/', null=False, blank=False)  # Make sure to create a 'blog_images' folder in your media directory



    