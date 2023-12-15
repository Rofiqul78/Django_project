"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from usermanagement.views import login_page
from django.conf.urls.static import static
from django.conf import settings
from viewsite.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('user/', include('usermanagement.urls')),
    path('', login_page),
    path('dashboard/', include('dashboard.urls')),
    path('blogs/', include('blogs.urls')),    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
