from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Persona
from .serializers import PersonaSerializer

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
#Buscar Persona por documento
class PersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
        persona = Persona.objects.filter(documento=documento).first()
        if not persona:
            raise NotFound('No se encontro una persona con ese documento.')
        serializers = PersonaSerializer(persona)
        return Response({'success': True, 'detail': 'Persona encontrada', 'data': serializers.data}, status=status.HTTP_200_OK)