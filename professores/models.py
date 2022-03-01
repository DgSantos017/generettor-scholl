from django.db import models

class CadastrarProfessores(models.Model):
    name_professor = models.CharField(max_length=255, unique=True)
