from rest_framework import serializers
from materias.serializers import MateriasSerializer

class ProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_professor = serializers.CharField()
    materias = MateriasSerializer(many=True)