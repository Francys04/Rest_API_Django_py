from django.db import models

# Create your models here.

# ctreate company model
class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=250, null=True, blank=True)
    
    # id added automatically
    def __str__(self):
        return self.name



class Advocate(models.Model):
    username = models.CharField(max_length=200)
    # null = True for db and blank=True for django 
    bio = models.TextField(max_length=250, null = True, blank=True)
    
    # create string of username return
    def __str__(self):
        return self.username
    
    
