from django.db import models

class ModelNikita(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    telephon = models.CharField(max_length=15)
    img = models.ImageField(upload_to='imgs')
