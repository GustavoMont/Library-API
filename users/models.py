from statistics import mode
from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.name