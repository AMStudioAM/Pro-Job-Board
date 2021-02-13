from django.contrib import admin

# Register your models here.
from .models import Job 

admin.site.register(Job) # Add Job To Admin Panel For Django Admin
