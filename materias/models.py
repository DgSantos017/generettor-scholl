from django.db import models
from professores.models import CadastrarProfessores

class RegisterMaterias(models.Model):
    name_materia = models.CharField(max_length=255, unique=True)
    qtd_aulas = models.IntegerField()
    professor = models.ManyToManyField(CadastrarProfessores, related_name='materias')
