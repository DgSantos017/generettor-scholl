from accounts.permissions import Instructor
from materias.models import RegisterMaterias
from .models import CadastrarProfessores
from .serializers import ProfessorSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
  
class Professores(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            name_professor = request.data['name_professor']
            professor = CadastrarProfessores.objects.create(name_professor=name_professor)
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data, status=201)

        except IntegrityError:
            return Response({"error": "Professor with this name already exists"}, status=400)

        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)
    

    def get(self, request):
        professor = CadastrarProfessores.objects.all()
        if professor:
            serializer = ProfessorSerializer(professor, many=True) 
            return Response(serializer.data, status=200)
        else:
            return {'Ainda não foi registrado nenhum professdor'}, 204


class ProfessorById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, professor_id):
        try:
            professor = CadastrarProfessores.objects.get(id=professor_id)
            name_professor = request.data['name_professor']
            professor.name_professor = name_professor
            professor.save()
            serializer = ProfessorSerializer(professor)

            return Response(serializer.data, status=200)
            
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)

        except CadastrarProfessores.DoesNotExist:
            return Response({'errors': 'invalid professor_id'}, status=404)

        except IntegrityError:
            return Response({"error": "Professor with this name already exists"}, status=400)


    def get(self, request, professor_id):
        try:
            professor = CadastrarProfessores.objects.get(id=professor_id)
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data, status=200)

        except CadastrarProfessores.DoesNotExist:
            return Response({'errors': 'invalid professor_id'}, status=404)

    def delete(self, request, professor_id):
        try:
            professor = CadastrarProfessores.objects.get(id=professor_id)
            professor.delete()

            return Response('', status=204)

        except CadastrarProfessores.DoesNotExist:
            return Response({'errors': 'invalid course_id'}, status=404)





        
    
