from django.urls import path
from .views import Professores, ProfessorById

urlpatterns = [
    path('professores/', Professores.as_view()),
    path('professor/<int:professor_id>', ProfessorById.as_view())
]