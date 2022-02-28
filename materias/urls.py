from django.urls import path
from .views import Materias, MateriaById

urlpatterns = [
    path('materias/', Materias.as_view()),
    path('materias/<int:materia_id>', MateriaById.as_view())
    
]