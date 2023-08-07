"""This module provides the necessary components to build and configure the admin interface for your Django application."""
from django.contrib import admin
"""This imports the Advocate and Company models from the same app. 
These models are likely defined in the models.py file of your app."""
from .models import Advocate, Company

# Register your models here.

admin.site.register(Advocate)
# company model
admin.site.register(Company)