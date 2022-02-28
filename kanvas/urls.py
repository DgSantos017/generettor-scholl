from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('professores.urls')),
    path('api/', include('materias.urls')),
    path('api/', include('turmas.urls'))
]
