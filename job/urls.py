from django.contrib import admin
from django.urls import path, include
from . import views # views for job application in my project

app_name = 'job' # this is app name to work with namespace and include 

urlpatterns = [
	path('', views.job_list, name="job_list"),
	path('<int:id>', views.job_detail, name="job_detail"), # this is not main url so, we have to name it with 'name' not 'namespace'
]