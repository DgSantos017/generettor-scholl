from accounts.permissions import Instructor
from materias.models import RegisterMaterias
from .models import RegisterTurmas
from .serializers import TurmaSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegistrationTurma(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, turma_id):
        try:
            turma = RegisterTurmas.objects.get(id=turma_id)
            id_materias = request.data['id_materias']
            
            if type(id_materias) == list:

                turma.materias.set([])

                for id in id_materias:
                    materia = RegisterMaterias.objects.get(id=id)
                    turma.materias.add(materia)
                
                materia.save()
                serializer = TurmaSerializer(turma)

                return Response(serializer.data)
            else:
                return Response({'error': 'you need to enter a list of turmas'}, 400)

        except RegisterTurmas.DoesNotExist:
            return Response({'errors': 'invalid id_turma'}, status=404)

        except RegisterMaterias.DoesNotExist:
            return Response({"error": "invalid materia_id list"}, status=404)

       
class Turmas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            name_turma = request.data['name_turma']
            turno = request.data['turno']

            turma = RegisterTurmas.objects.create(name_turma=name_turma, turno=turno)
            serializer = TurmaSerializer(turma)
            return Response(serializer.data, status=201)

        except IntegrityError:
            return Response({"error": "Turma with this name already exists"}, status=400)

        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)
    

    def get(self, request):
        
        turma = RegisterTurmas.objects.all()
        if turma:
            serializer = TurmaSerializer(turma, many=True) 
            return Response(serializer.data, status=200)
        else:
            return {'Ainda não foi registrado nenhuma turma'}, 204


class TurmaById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, turma_id):
        try:
            turma = RegisterTurmas.objects.get(id=turma_id)
            name_turma = request.data['name_turma']
            turma.name_turma = name_turma
            turma.save()
            serializer = TurmaSerializer(turma)

            return Response(serializer.data, status=200)
            
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)

        except RegisterTurmas.DoesNotExist:
            return Response({'errors': 'invalid turma_id'}, status=404)

        except IntegrityError:
            return Response({"error": "Turma with this name already exists"}, status=400)


    def get(self, request, turma_id):
        try:
            turma = RegisterTurmas.objects.get(id=turma_id)
            serializer = TurmaSerializer(turma)
            return Response(serializer.data, status=200)

        except RegisterTurmas.DoesNotExist:
            return Response({'errors': 'invalid turma_id'}, status=404)

    def delete(self, request, turma_id):
        try:
            turma = RegisterTurmas.objects.get(id=turma_id)
            turma.delete()

            return Response('', status=204)

        except RegisterTurmas.DoesNotExist:
            return Response({'errors': 'invalid turma_id'}, status=404)





        
    
