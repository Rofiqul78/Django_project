from django.db import models
from django.utils import timezone

class BlogTables(models.Model):
    student_name = models.CharField(max_length=100, null=False, blank=False)
    order_number = models.IntegerField(default=0)
    imageField = models.ImageField(upload_to='image/') # Make sure to create a 'blog_images' folder in your media directory
    Created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
        
def __str__(self): 
    return self.order_number        
    

