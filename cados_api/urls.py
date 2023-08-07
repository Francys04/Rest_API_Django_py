"""
URL configuration for cados_api project.

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
"""Imports the admin module from django.contrib, which provides the Django administration site."""
from django.contrib import admin
""" Imports the path function for defining URL patterns and the include 
function for including other URL configuration modules."""
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Maps the URL pattern 'admin/' to the Django admin site. 
    # When a user navigates to http://yourdomain.com/admin/, they will access the Django admin interface.
    # create new path
    path('', include('base.urls'))
]
"""It uses the include function to include the URL configuration from the 'base.urls' module. 
This means that any URLs defined in the base.urls module will be included under the root URL."""