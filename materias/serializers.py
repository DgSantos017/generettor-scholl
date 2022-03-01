from rest_framework import serializers
from professores.serializers import ProfessorSerializer

class MateriasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_materia = serializers.CharField()
    qtd_aulas = serializers.IntegerField()
    professores = ProfessorSerializer(many=True)