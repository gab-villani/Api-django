from rest_framework import serializers
from app.models import Carro


class Carroserializer(serializers.ModelSerializer):
    class Meta:

        model = Carro
        fields =['id','marca','modelo', 'bits']