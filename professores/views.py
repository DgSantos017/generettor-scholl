from accounts.permissions import Instructor
from materias.models import RegisterMaterias
from .models import CadastrarProfessores
from .serializers import ProfessorSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegistrationProfessor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, professor_id):
        try:
            professor = CadastrarProfessores.objects.get(id=professor_id)
            id_materias = request.data['id_materias']
            
            if type(id_materias) == list:

                professor.materias.set([])

                for id in id_materias:
                    materia = RegisterMaterias.objects.get(id=id)
                    professor.materias.add(materia)
                
                professor.save()
                serializer = ProfessorSerializer(professor)

                return Response(serializer.data)
            else:
                return Response({'error': 'you need to enter a list of materias'}, 400)

        except CadastrarProfessores.DoesNotExist:
            return Response({'errors': 'invalid id_materia'}, status=404)

        except RegisterMaterias.DoesNotExist:
            return Response({"error": "invalid materia_id list"}, status=404)

       
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


# class CourseById(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [Instructor]

#     def put(self, request, course_id):
#         try:
#             course = Course.objects.get(id=course_id)
#             name = request.data['name']
#             course.name = name
#             course.save()
#             serializer = CourseSerializer(course)

#             return Response(serializer.data, status=200)
            
#         except KeyError as e:
#             return Response({"error": f"{str(e)} is missing"}, status=400)

#         except Course.DoesNotExist:
#             return Response({'errors': 'invalid course_id'}, status=404)

#         except IntegrityError:
#             return Response({"error": "Course with this name already exists"}, status=400)


#     def get(self, request, course_id):
#         try:
#             course = Course.objects.get(id=course_id)
#             serializer = CourseSerializer(course)
#             return Response(serializer.data, status=200)

#         except Course.DoesNotExist:
#             return Response({'errors': 'invalid course_id'}, status=404)

#     def delete(self, request, course_id):
#         try:
#             course = Course.objects.get(id=course_id)
#             course.delete()

#             return Response('', status=204)

#         except Course.DoesNotExist:
#             return Response({'errors': 'invalid course_id'}, status=404)





        
    
