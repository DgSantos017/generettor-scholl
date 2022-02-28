from django.db import models
from professores.models import CadastrarProfessores

class RegisterTurmas(models.Model):
    name_turma = models.CharField(max_length=255, unique=True)
    turno = models.CharField(max_length=255)
    professores = models.ManyToManyField(CadastrarProfessores, related_name='turmas')


