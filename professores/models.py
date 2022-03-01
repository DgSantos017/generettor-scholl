from django.db import models
# from materias.models import RegisterMaterias

class CadastrarProfessores(models.Model):
    name_professor = models.CharField(max_length=255, unique=True)
    # materias = models.ManyToManyField(RegisterMaterias, related_name='professores')
