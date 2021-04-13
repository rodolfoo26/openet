from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    matricula = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    curso = models.CharField(max_length=100)

