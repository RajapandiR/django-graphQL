from django.db import models

# Create your models here.

class Stud(models.Model):
	name = models.CharField(max_length=20, unique=True, null=True)
	age = models.IntegerField(null=True)
	file = models.FileField(upload_to="uploads", null=True)
	create_at = models.DateTimeField(auto_now_add = True, null=True)

	def __str__(self):
		return self.name