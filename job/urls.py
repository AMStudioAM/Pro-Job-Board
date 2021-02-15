from django.contrib import admin
from django.urls import path, include
from . import views # views for job application in my project


urlpatterns = [
	path('', views.job_list),
	path('<int:id>', views.job_detail),
]