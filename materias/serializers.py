from rest_framework import serializers

class MateriasSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_materia = serializers.CharField()
    qtd_aulas = serializers.IntegerField()
    professor = serializers.CharField()