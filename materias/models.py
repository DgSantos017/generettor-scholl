from django.db import models
 
class RegisterMaterias(models.Model):
    name_materia = models.CharField(max_length=255, unique=True)
    qtd_aulas = models.IntegerField()
    professor = models.CharField(max_length=255)