from accounts.permissions import Instructor
from .models import RegisterMaterias
from .serializers import MateriasSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ComplementMateria(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, materia_id):
        try:
            materia = RegisterMaterias.objects.get(id=materia_id)

            qtd_aulas = request.data['qtd_aulas']
            professor = request.data['professor']

            materia.qtd_aulas = qtd_aulas
            materia.professor = professor

            materia.save()
            serializer = MateriasSerializer(materia)

            return Response(serializer.data, status=200)
            
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)

        except RegisterMaterias.DoesNotExist:
            return Response({'errors': 'invalid materia_id'}, status=404)

        except IntegrityError:
            return Response({"error": "Materia with this name already exists"}, status=400)


class Materias(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            name_materia = request.data['name_materia']
    
            materia = RegisterMaterias.objects.create(name_materia=name_materia, qtd_aulas = 0, professor = "")
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


class MateriaById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, materia_id):
        try:
            materia = RegisterMaterias.objects.get(id=materia_id)
            name_materia = request.data['name_materia']
            materia.name_materia = name_materia
            materia.save()
            serializer = MateriasSerializer(materia)

            return Response(serializer.data, status=200)
            
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)

        except RegisterMaterias.DoesNotExist:
            return Response({'errors': 'invalid materia_id'}, status=404)

        except IntegrityError:
            return Response({"error": "Materia with this name already exists"}, status=400)


    def get(self, request, materia_id):
        try:
            materia = RegisterMaterias.objects.get(id=materia_id)
            serializer = MateriasSerializer(materia)
            return Response(serializer.data, status=200)

        except RegisterMaterias.DoesNotExist:
            return Response({'errors': 'invalid materia_id'}, status=404)

    def delete(self, request, materia_id):
        try:
            materia = RegisterMaterias.objects.get(id=materia_id)
            materia.delete()

            return Response('', status=204)

        except RegisterMaterias.DoesNotExist:
            return Response({'errors': 'invalid materia_id'}, status=404)







        
    

