from django.db import models

"""
django model field
	- html widget (Done)
	- validation
	- db size (Max Length And Min Length)
"""

# Create your models here.

JOB_TYPE = (
	("FULL TIME", "FULL TIME"),
	("PART TIME", "PART TIME"),
)

def image_upload(instance, filename):
	imagename, extension = filename.split(".")
	return "jobs/%s.%s"%(instance.id, extension) 

class Job(models.Model): # table
	title = models.CharField(max_length=100) # column
	# location
	job_type = models.CharField(max_length=15, choices=JOB_TYPE) # column
	description = models.TextField(max_length=1000) # column
	published_at = models.DateTimeField(auto_now=True) # column
	Vacancy = models.IntegerField(default=1) # column
	salary = models.IntegerField(default=0) # column
	expereince = models.IntegerField(default=1) # column
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload)


	def __str__(self):
		return f"{self.title} | Expereince {self.expereince} Year"

class Category(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name