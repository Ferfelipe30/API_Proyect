from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        if not personas:
            raise NotFound("No se encontraron personas.")
        return Response({'success': True, 'detail': 'Listado de personas', 'data': serializer.data}, status=status.HTTP_200_OK)

class CrearPersona(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data':serializer.data}, status=status.HTTP_201_CREATED)

class ActualizarPersona(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def put(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        email = request.data.get('email', None)

        #Verificar si el email ha cambiado
        if email and email != persona.email:
            # Verificar si ya existe otra persona con el mismo email
            if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                return Response({'email': ['Persona with this email already exists.']}, status=status.HTTP_400_BAD_REQUEST)
            
        serializers = PersonaSerializer(persona, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({'success': True, 'detail': 'Persona actualizada correctamente.', 'data': serializers.data}, status=status.HTTP_200_OK)

class EliminarPersona(generics.DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def delete(self, request, pk):
        
        persona = get_object_or_404(Persona, pk=pk)
        persona.delete()
        return Response({'success': True, 'detail': 'Persona eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

#Buscar Persona por documento
class PersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
        persona = Persona.objects.filter(documento=documento).first()
        if not persona:
            raise NotFound('No se encontro una persona con ese documento.')
        serializers = PersonaSerializer(persona)
        return Response({'success': True, 'detail': 'Persona encontrada', 'data': serializers.data}, status=status.HTTP_200_OK)
    
class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    
    def list(self, request):
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        if not tareas:
            raise NotFound("No se encontraron tareas.")
        return Response({'success': True, 'detail': 'Listado de tareas', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class CrearTarea(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
class ActualizarTarea(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        serializer = TareaSerializer(tarea, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Tarea actualizada correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)
    

class EliminarTarea(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def delete(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        tarea.delete()
        return Response({'success': True, 'detail': 'Tarea eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
class TareaByFechaLimite(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get(self, request, fecha_limite):
        tarea = Tarea.objects.filter(fecha_limite=fecha_limite).first()
        if not tarea:
            raise NotFound('No se encontro una tarea con esa fecha limite.')
        serializer = TareaSerializer(tarea)
        return Response({'success': True, 'detail': 'Tarea encontrada', 'data': serializer.data}, status=status.HTTP_200_OK)