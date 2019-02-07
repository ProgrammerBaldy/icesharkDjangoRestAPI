from django.db import models

# Create your models here.

class valorModel(models.Model):
	valor_banco_brasil = models.BigIntegerField()
	valor_banco_bradesco = models.BigIntegerField()