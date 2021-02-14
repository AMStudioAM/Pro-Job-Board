from django.contrib import admin

# Register your models here.
from .models import Job, Category

admin.site.register(Job) # Add Job To Admin Panel For Django Admin
admin.site.register(Category) # Add Category To Admin Panel
