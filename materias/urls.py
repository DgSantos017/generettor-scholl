from django.urls import path
from .views import Materias

urlpatterns = [
    path('materias/', Materias.as_view())
]