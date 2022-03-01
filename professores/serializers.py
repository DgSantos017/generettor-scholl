from rest_framework import serializers

class ProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name_professor = serializers.CharField()
   