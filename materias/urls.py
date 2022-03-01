from django.urls import path
from .views import Materias, MateriaById, RegistrationMateria

urlpatterns = [
    path('materia/<int:materia_id>/professores/', RegistrationMateria.as_view()),
    path('materias/', Materias.as_view()),
    path('materia/<int:materia_id>', MateriaById.as_view())
    
]