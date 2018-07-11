from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Header(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	button = models.CharField(max_length=20)
	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Service_Section(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=4000)
	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Column(models.Model):
	
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=4000)
	def __str__(self):
		return self.title
