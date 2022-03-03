from django.db import models
from django.contrib.auth.models import User


class RegisterMaterias(models.Model):
    name_materia = models.CharField(max_length=255, unique=True)
    qtd_aulas = models.IntegerField()
    professor = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)