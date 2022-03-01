from rest_framework import serializers
from materias.serializers import MateriasSerializer

class TurmaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_turma = serializers.CharField()
    turno = serializers.CharField()
    materias = MateriasSerializer(many=True)