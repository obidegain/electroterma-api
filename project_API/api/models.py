from django.db import models

# Create your models here.

# Create your models here.
class Temperature(models.Model):
	temperature 		= models.IntegerField(null=False, blank=True)
	reference 			= models.TextField(max_length=5000, null=False, blank=True)
	def __str__(self):
		return self.reference