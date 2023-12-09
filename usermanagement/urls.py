# from django.contrib import admin

from django.urls import path, include

# from university_app.views import index

from .views import login_page

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login_page),
]