from rest_framework import serializers
from professores.serializers import ProfessorSerializer

class TurmaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_turma = serializers.CharField()
    turno = serializers.CharField()
    professores = ProfessorSerializer(many=True)