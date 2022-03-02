from django.urls import path
from .views import Materias, MateriaById, ComplementMateria

urlpatterns = [
    path('materia/<int:materia_id>/complement/', ComplementMateria.as_view()),
    path('materias/', Materias.as_view()),
    path('materia/<int:materia_id>', MateriaById.as_view())
]