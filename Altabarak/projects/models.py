from __future__ import unicode_literals
from django.db import models


# Create your models here.
class senddata(models.Model):
	Job_title = models.CharField(max_length=60)
	Edu_Qualification = models.CharField(max_length=100)
	years_of_Experience = models.CharField(max_length=2)
	pub_date = models.DateField()

	def __str__(self):
		return self.Job_title


class Document(models.Model):
    description = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    empemail = models.EmailField()
    phonenumber = models.CharField(max_length=50, blank=True)


class ContactUs(models.Model):
	fullname = models.CharField(max_length=60)
	e_mail = models.EmailField()
	text = models.CharField(max_length=500)
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.fullname





