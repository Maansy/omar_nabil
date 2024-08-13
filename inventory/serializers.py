from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MechanicalPart, RawMaterial, ElectricalPart

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class MechanicalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechanicalPart
        fields = '__all__'

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class ElectricalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricalPart
        fields = '__all__'
