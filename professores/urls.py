from django.urls import path
from .views import Professores, RegistrationProfessor

urlpatterns = [
    path('courses/<int:professor_id>/registrations/', RegistrationProfessor.as_view()),
    path('professores/', Professores.as_view()) 

    # path('courses/', Courses.as_view())
]