from rest_framework import serializers
from accounts.serializers import UserSerializer

class MateriasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_materia = serializers.CharField()
    qtd_aulas = serializers.IntegerField()