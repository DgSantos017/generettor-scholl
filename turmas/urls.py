from django.urls import path
from .views import Turmas, RegistrationTurma, TurmaById

urlpatterns = [
    path('turma/<int:turma_id>', TurmaById.as_view()),
    path('turma/<int:turma_id>/materias/', RegistrationTurma.as_view()),
    path('turmas/', Turmas.as_view()) 
]