from django.urls import path
from .views import Materias, MateriaById, RegistrationMateria, QtdAulas

urlpatterns = [
    path('materia/<int:materia_id>/professor/', RegistrationMateria.as_view()),
    path('materias/', Materias.as_view()),
    path('materia/<int:materia_id>', MateriaById.as_view()),
    path('materia/<int:materia_id>/aulas/', QtdAulas.as_view())
    
]