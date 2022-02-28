from django.contrib.auth.models import User
from accounts.permissions import Instructor
from .models import RegisterMaterias
from .serializers import MateriasSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
class Materias(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            name_materia = request.data['name_materia']
    
            materia = RegisterMaterias.objects.create(name_materia=name_materia, qtd_aulas = 0)
            serializer = MateriasSerializer(materia)
            return Response(serializer.data, status=201)

        except IntegrityError:
            return Response({"error": "Materia with this name already exists"}, status=409)

        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)
    

    def get(self, request):
        materias = RegisterMaterias.objects.all()
        if materias:
            serializer = MateriasSerializer(materias, many=True) 
            return Response(serializer.data, status=200)
        else:
            return {'Ainda não foi registrado nenhuma materia'}, 204







        
    
