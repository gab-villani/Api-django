from rest_framework import viewsets
from app.models import Carro
from app.serializer import Carroserializer

class CarroViewsSet(viewsets.ModelViewSet):
    queryset= Carro.objects.all()
    serializer_class= Carroserializer


