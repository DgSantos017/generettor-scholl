from django.urls import path
from .views import Professores, RegistrationProfessor

urlpatterns = [
    path('professores/<int:professor_id>/materias/', RegistrationProfessor.as_view()),
    path('professores/', Professores.as_view()) 
]