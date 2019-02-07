from django.db import models

# Create your models here.
class news(models.Model):
	title = models.CharField(max_length = 40)
	text = models.CharField(max_length = 1000)
	date = models.CharField(max_length = 20)

	def __str__(self):
		return self.title