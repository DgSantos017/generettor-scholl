from django.db import models
from materias.models import RegisterMaterias
from django.contrib.auth.models import User


class RegisterTurmas(models.Model):
    name_turma = models.CharField(max_length=255, unique=True)
    turno = models.CharField(max_length=255)
    materias = models.ManyToManyField(RegisterMaterias, related_name='turmas')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


