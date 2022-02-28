from django.urls import path
from .views import Turmas, RegistrationTurma

urlpatterns = [
    path('turmas/<int:turma_id>/professores/', RegistrationTurma.as_view()),
    path('turmas/', Turmas.as_view()) 
]